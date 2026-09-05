"""
SONIQ MASTER AI
Background job queue.

Provides Redis/RQ queue configuration for
asynchronous mastering jobs.
"""

import os

from redis import Redis
from rq import Queue


def get_redis_connection() -> Redis:
    """
    Create a Redis connection using environment settings.
    """

    redis_url = os.getenv(
        "REDIS_URL",
        "redis://redis:6379/0",
    )

    return Redis.from_url(
        redis_url,
        decode_responses=True,
    )


def get_queue(
    name: str = "soniq-mastering",
) -> Queue:
    """
    Return the mastering job queue.
    """

    connection = get_redis_connection()

    return Queue(
        name=name,
        connection=connection,
    )


mastering_queue = get_queue()
