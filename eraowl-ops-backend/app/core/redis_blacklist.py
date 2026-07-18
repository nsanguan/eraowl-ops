"""
Redis-backed token blacklist.

Blacklists JWT access tokens by storing a hash of the token
in Redis with a TTL matching the token's remaining lifetime.
"""

from __future__ import annotations

import hashlib
import logging
from datetime import datetime, timezone

import redis.asyncio as aioredis

from app.core.config import settings

logger = logging.getLogger("eraowl-ops")


def _token_key(token_hash: str) -> str:
    return f"bl:{token_hash}"


async def blacklist_token(token: str, ttl_seconds: int) -> bool:
    """
    Add a token to the Redis blacklist.

    Args:
        token: The raw JWT access token.
        ttl_seconds: Time-to-live in seconds (token's remaining lifetime).

    Returns:
        True if successfully blacklisted, False on failure.
    """
    try:
        r = await aioredis.from_url(settings.REDIS_URL, decode_responses=True)
        token_hash = hashlib.sha256(token.encode()).hexdigest()
        key = _token_key(token_hash)
        # Store the current timestamp as value (for auditing)
        now_ts = datetime.now(timezone.utc).timestamp()
        await r.set(key, str(now_ts), ex=ttl_seconds)
        await r.aclose()
        return True
    except Exception as exc:
        logger.warning("Failed to blacklist token in Redis: %s", exc)
        return False


async def is_token_blacklisted(token: str) -> bool:
    """
    Check if a token has been blacklisted.

    Args:
        token: The raw JWT access token.

    Returns:
        True if the token is blacklisted, False otherwise.
    """
    try:
        r = await aioredis.from_url(settings.REDIS_URL, decode_responses=True)
        token_hash = hashlib.sha256(token.encode()).hexdigest()
        key = _token_key(token_hash)
        exists = await r.exists(key)
        await r.aclose()
        return bool(exists)
    except Exception as exc:
        logger.warning("Redis blacklist check failed: %s", exc)
        return False
