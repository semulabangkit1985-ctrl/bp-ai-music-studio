"""
SONIQ MASTER AI
Audio upload routes.
"""

from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, File, HTTPException, UploadFile, status

from ..config import settings

router = APIRouter(
    prefix="/upload",
    tags=["Audio Upload"],
)

ALLOWED_EXTENSIONS = {
    ".wav",
    ".mp3",
    ".flac",
    ".aiff",
    ".aif",
    ".m4a",
}


@router.post("/")
async def upload_audio(file: UploadFile = File(...)):
    """
    Upload an audio file for mastering.
    """

    if not file.filename:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No filename provided.",
        )

    extension = Path(file.filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Unsupported audio format.",
        )

    upload_dir = Path(settings.upload_dir)
    upload_dir.mkdir(parents=True, exist_ok=True)

    file_id = uuid4().hex
    safe_filename = f"{file_id}{extension}"
    file_path = upload_dir / safe_filename

    max_size = settings.max_upload_size_mb * 1024 * 1024
    total_size = 0

    try:
        with file_path.open("wb") as output:
            while chunk := await file.read(1024 * 1024):
                total_size += len(chunk)

                if total_size > max_size:
                    file_path.unlink(missing_ok=True)

                    raise HTTPException(
                        status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
                        detail="Audio file is too large.",
                    )

                output.write(chunk)

    finally:
        await file.close()

    return {
        "status": "uploaded",
        "file_id": file_id,
        "filename": file.filename,
        "format": extension.replace(".", ""),
        "size_bytes": total_size,
        "path": str(file_path),
    }
