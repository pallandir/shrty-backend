from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Type

from app.database.repositories.base import Repository
from . import ModelType


class URLRepository(Repository[ModelType]):
    def __init__(self, session: AsyncSession, model: Type[ModelType]):
        super().__init__(session=session, model=model)

    async def get_mapped_url(self, mapped_url: str) -> dict:
        result = await self.session.execute(
            select(self.model).where(self.model.mapped_url == mapped_url)
        )
        return result.scalars().first()
