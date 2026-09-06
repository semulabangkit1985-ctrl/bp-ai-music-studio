"""
SONIQ MASTER AI
Background worker queue.

Provides a simple Redis/RQ queue for audio mastering jobs.
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
        "redis://localhost:6379/0",
    )

    return Redis.from_url(
        redis_url,
        decode_responses=False,
    )


def get_mastering_queue() -> Queue:
    """
    Return the queue used for mastering jobs.
    """

    connection = get_redis_connection()

    return Queue(
        name="soniq-mastering",
        connection=connection,
        default_timeout=3600,
    )


mastering_queue = get_mastering_queue()
