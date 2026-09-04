"""
SONIQ MASTER AI
API middleware configuration.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def setup_middleware(app: FastAPI) -> FastAPI:
    """
    Configure middleware for the SONIQ MASTER AI API.
    """

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
