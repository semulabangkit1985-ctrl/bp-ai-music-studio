"""
SONIQ MASTER AI
Master download routes.
"""

from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from ..config import settings

router = APIRouter(
    prefix="/downloads",
    tags=["Downloads"],
)


@router.get("/{filename}")
async def download_master(filename: str):
    """
    Download a mastered audio file.
    """

    master_dir = Path(settings.master_dir)
    file_path = master_dir / filename

    if not file_path.exists() or not file_path.is_file():
        raise HTTPException(
            status_code=404,
            detail="Mastered audio file not found.",
        )

    return FileResponse(
        path=file_path,
        filename=file_path.name,
        media_type="application/octet-stream",
    )
