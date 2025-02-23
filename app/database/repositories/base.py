from typing import Type, Generic, List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select
from sqlalchemy import delete, update


from app.exceptions import DBInsertError
from app.exceptions.messages import GENERIC_ERROR_MESSAGE
from . import ModelType


class Repository(Generic[ModelType]):
    def __init__(self, session: AsyncSession, model: Type[ModelType]):
        self.session = session
        self.model = model

    async def create(self, obj: ModelType) -> ModelType:
        try:
            self.session.add(obj)
            await self.session.commit()
        except IntegrityError as integrity_error:
            raise DBInsertError(f"{GENERIC_ERROR_MESSAGE}{integrity_error.orig}")
        await self.session.refresh(obj)
        return obj

    async def get_all(self) -> List[ModelType]:
        result = await self.session.execute(select(self.model))
        return result.scalars().all()

    async def get_by_id(self, obj_id: int) -> Optional[ModelType]:
        result = await self.session.execute(
            select(self.model).where(self.model.id == obj_id)
        )
        return result.scalars().first()

    async def update_model(self, obj_id: int, obj: ModelType) -> Optional[ModelType]:
        changed_attributes = {
            key: value
            for key, value in obj.__dict__.items()
            if key != "_sa_instance_state"
        }
        await self.session.execute(
            update(self.model).where(self.model.id == obj_id).values(changed_attributes)
        )
        await self.session.commit()
        return await self.get_by_id(obj_id)

    async def delete_model(self, obj_id: int) -> bool:
        result = await self.session.execute(
            delete(self.model).where(self.model.id == obj_id)
        )
        await self.session.commit()
        return result.rowcount > 0  # Returns True if a row was deleted
