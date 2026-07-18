"""
Shared rate limiter instance (slowapi).

Exported so any module can apply @limiter.limit() to sensitive endpoints.
"""
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
