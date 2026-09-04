"""
SONIQ MASTER AI
Mastering API routes.
"""

from pathlib import Path

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter(
    prefix="/mastering",
    tags=["AI Mastering"],
)


class MasteringRequest(BaseModel):
    file_id: str
    preset: str = "universal"
    target_lufs: float = -14.0
    true_peak_db: float = -1.0
    vocal_safe: bool = True


@router.post("/")
async def start_mastering(request: MasteringRequest):
    """
    Start an AI mastering job.
    """

    upload_dir = Path("storage/uploads")
    matching_files = list(upload_dir.glob(f"{request.file_id}.*"))

    if not matching_files:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Audio file not found.",
        )

    return {
        "status": "queued",
        "file_id": request.file_id,
        "preset": request.preset,
        "target_lufs": request.target_lufs,
        "true_peak_db": request.true_peak_db,
        "vocal_safe": request.vocal_safe,
        "message": "AI mastering job has been queued.",
    }
