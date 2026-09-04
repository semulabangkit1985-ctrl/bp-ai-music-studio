"""
SONIQ MASTER AI
API dependencies.
"""

from collections.abc import Generator

from sqlalchemy.orm import Session

from .database import get_db


def get_database() -> Generator[Session, None, None]:
    """
    Provide a database session for API routes.
    """
    yield from get_db()
