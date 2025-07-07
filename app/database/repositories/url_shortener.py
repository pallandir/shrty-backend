from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Type

from app.database.repositories.base import Repository
from . import ModelType


class URLRepository(Repository[ModelType]):
    def __init__(self, session: AsyncSession, model: Type[ModelType]):
        super().__init__(session=session, model=model)

    async def get_mapped_url(
        self, mapped_url: str, field_to_check: str = "mapped_url"
    ) -> dict:
        result = await self.session.execute(
            select(self.model).where(getattr(self.model, field_to_check) == mapped_url)
        )
        return result.scalars().first()
