import random
import string
from fastapi import APIRouter, status, Path, HTTPException, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime

from logger import CustomLogger
from app.database.session import get_db_session
from app.database.repositories.url_shortener import URLRepository
from app.exceptions import DBInsertError
from .schema import URL, URLResponse
from .service import filtered_emojis
from .model import URLORM

router = APIRouter(tags=["url shortener"])
LOGGER = CustomLogger(module_name=__name__).get_logger()
URL_LENGTH = 4


async def get_url_repository(session: AsyncSession = Depends(get_db_session)):
    return URLRepository(session=session, model=URLORM)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    description="Create a new shortened URL",
    summary="Create a new shortened URL from a Http URL. An optional parameter can be sent to suggest your own shortened URL",
    responses={
        status.HTTP_200_OK: {
            "model": URLResponse,
            "description": "Shortened URL",
        },
    },
)
async def create_url_mapping(
    url: URL,
    repository: URLRepository[URLORM] = Depends(get_url_repository),
):
    available_chars = (
        f"{string.ascii_uppercase}:{string.digits}{''.join(filtered_emojis())}"
    )
    shortened_url = "".join(random.choices(available_chars, k=URL_LENGTH))
    shortened_url_model = URLResponse(
        short_url=shortened_url, mapped_url=url.url
    ).model_dump(mode="json")
    try:
        check_mapped_url = await repository.get_mapped_url(
            shortened_url_model.get("mapped_url", "")
        )
        if check_mapped_url:
            shortened_url_model = check_mapped_url.__dict__
        else:
            await repository.create(URLORM(**shortened_url_model))
    except DBInsertError as insert_error:
        LOGGER.exception(insert_error)
        raise HTTPException(status.HTTP_400_BAD_REQUEST, insert_error.message)

    return shortened_url_model


@router.get(
    "/{url}",
    status_code=status.HTTP_200_OK,
    description="Redirect a shortened URL to a mapped URL",
    summary="Redirect a shortened URL to a mapped URL",
    responses={
        status.HTTP_301_MOVED_PERMANENTLY: {
            "description": "Redirected",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "No mapped URL found",
        },
    },
)
async def redirect_mapped_url(
    url: str = Path(),
    repository: URLRepository[URLORM] = Depends(get_url_repository),
):
    try:
        mapped_url = await repository.get_mapped_url(url, "short_url")
        if mapped_url:
            mapped_url.visited += 1
            mapped_url.last_visit = datetime.now().date()
            await repository.update_model(mapped_url.id, mapped_url)
            return RedirectResponse(mapped_url.mapped_url)
    except DBInsertError as insert_error:
        LOGGER.exception(insert_error)
        raise HTTPException(status.HTTP_400_BAD_REQUEST, insert_error.message)
