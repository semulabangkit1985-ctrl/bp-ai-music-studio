"""
SONIQ MASTER AI
Main API application.
"""

from fastapi import FastAPI

from .logging_config import setup_logging
from .middleware import setup_middleware

from .routes.auth import router as auth_router
from .routes.upload import router as upload_router
from .routes.analysis import router as analysis_router
from .routes.mastering import router as mastering_router
from .routes.presets import router as presets_router
from .routes.projects import router as projects_router
from .routes.downloads import router as downloads_router
from .routes.health import router as health_router


def create_app() -> FastAPI:
    """
    Create and configure the SONIQ MASTER AI API.
    """

    setup_logging()

    app = FastAPI(
        title="SONIQ MASTER AI",
        description=(
            "AI-powered audio mastering platform "
            "with vocal-safe processing."
        ),
        version="1.0.0",
    )

    setup_middleware(app)

    app.include_router(
        auth_router
    )

    app.include_router(
        upload_router
    )

    app.include_router(
        analysis_router
    )

    app.include_router(
        mastering_router
    )

    app.include_router(
        presets_router
    )

    app.include_router(
        projects_router
    )

    app.include_router(
        downloads_router
    )

    app.include_router(
        health_router
    )

    @app.get("/")
    async def root():
        return {
            "name": "SONIQ MASTER AI",
            "status": "online",
            "version": "1.0.0",
            "message": "SONIQ MASTER AI API is running.",
        }

    return app


app = create_app()
