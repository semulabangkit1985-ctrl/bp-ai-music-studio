"""
SONIQ MASTER AI
Main API application.
"""

from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(
        title="SONIQ MASTER AI",
        description="AI-powered audio mastering platform.",
        version="1.0.0",
    )

    @app.get("/")
    async def root():
        return {
            "name": "SONIQ MASTER AI",
            "status": "online",
            "version": "1.0.0",
        }

    @app.get("/health")
    async def health():
        return {
            "status": "healthy"
        }

    return app


app = create_app()
