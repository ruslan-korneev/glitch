from typing import TYPE_CHECKING, Optional, cast

import redis.asyncio as redis

from src.config.const import REDIS_DB, REDIS_HOST, REDIS_PORT

if TYPE_CHECKING:
    from src.db.models.users import User

redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_DB,
)


class Redis:
    """
    Redis wrapper
    adding a prefix to keys which supposed to be user's id
    """

    client: redis.Redis

    def __init__(self, user: Optional["User"] = None) -> None:
        self.client = redis_client
        self.user_id = user.pk if user else None

    def _key(self, key: str) -> str:
        """Get redis key"""
        if self.user_id is not None:
            key = f"{self.user_id}:{key}"
        return key

    async def get(self, key: str, __default: str | None = None) -> str | None:
        """Get value from redis"""
        value = await self.client.get(self._key(key))
        value = cast(bytes | None, value)
        return value.decode() if value is not None else __default

    async def set(self, key: str, value: str) -> bool:
        """Set value to redis"""
        success = await self.client.set(self._key(key), value)
        success = cast(bool, success)
        return success

    async def delete(self, key: str) -> int:
        """Delete value from redis"""
        deleted_amount = await self.client.delete(self._key(key))
        deleted_amount = cast(int, deleted_amount)
        return deleted_amount

    async def pop(self, key: str, __default: str | None = None) -> str | None:
        """Pop value from redis"""
        if not await self.exists(key):
            return __default

        value = await self.get(key)
        await self.delete(key)
        return value

    async def incr(self, key: str) -> int:
        """Increment value in redis"""
        return await self.client.incr(self._key(key))

    async def decr(self, key: str) -> int:
        """Decrement value in redis"""
        return await self.client.decr(self._key(key))

    async def exists(self, key: str) -> int:
        """Check if key exists in redis"""
        return await self.client.exists(self._key(key))
