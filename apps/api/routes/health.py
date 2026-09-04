"""
SONIQ MASTER AI
Health check routes.
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("/")
async def health_check():
    """
    Check API health status.
    """

    return {
        "status": "healthy",
        "service": "SONIQ MASTER AI API",
        "version": "1.0.0",
    }


@router.get("/ready")
async def readiness_check():
    """
    Check whether the API is ready to process requests.
    """

    return {
        "status": "ready",
        "service": "SONIQ MASTER AI API",
    }
