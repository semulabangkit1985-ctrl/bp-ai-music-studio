"""
SONIQ MASTER AI
Authentication routes.
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.get("/status")
async def auth_status():
    return {
        "status": "ready",
        "message": "Authentication service is ready.",
    }
