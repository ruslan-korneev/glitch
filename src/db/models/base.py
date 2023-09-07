from typing import Any, Self, Sequence, cast

from sqlalchemy import Column, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.config.db import Base


class CRUDModel(Base):
    """
    Base class for all CRUD models
    CRUD models are used to create, read, update and delete data
    """

    __abstract__ = True

    async def save(self, session: AsyncSession) -> Self:
        session.add(self)
        await session.commit()
        return self

    async def delete(self, session: AsyncSession) -> None:
        await session.delete(self)
        await session.commit()

    async def update(self, session: AsyncSession, **kwargs) -> Self:
        for key, value in kwargs.items():
            setattr(self, key, value)

        self = await self.save(session)
        await session.refresh(self)
        return self

    @classmethod
    async def get_all(cls, session: AsyncSession) -> Sequence[Self]:
        query = select(cls)
        result = await session.execute(query)
        return result.scalars().all()

    @classmethod
    async def get_by_pk(cls, session: AsyncSession, pk: Any) -> Self | None:
        return await session.get(cls, pk)

    @classmethod
    def get_pk_column(cls) -> Column:
        pk = cast(Any, cls.__table__.primary_key)
        return pk.columns[0]

    @property
    def pk(self) -> Any:
        return getattr(self, self.get_pk_column().name)
