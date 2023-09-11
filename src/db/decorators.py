import functools
from typing import Any, Protocol

from sqlalchemy.ext.asyncio import AsyncSession

from src.db import get_session

__all__ = [
    "include_session",
]


class DBQueryCallableRequireSession(Protocol):
    async def __call__(self, session: AsyncSession, **kwargs: Any) -> Any:
        ...


class DBQueryCallableNoNeedSession(Protocol):
    async def __call__(self, **kwargs: Any) -> Any:
        ...


def include_session(
    func: DBQueryCallableRequireSession,
) -> DBQueryCallableNoNeedSession:
    """
    Decorator for async functions that insert session into function arguments
    """

    @functools.wraps(func)
    async def wrapper(**kwargs: Any) -> Any:
        result = None
        async for session in get_session():
            result = await func(session=session, **kwargs)
        return result

    return wrapper
