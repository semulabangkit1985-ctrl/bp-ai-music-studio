"""
SONIQ MASTER AI
Audio service.

Handles basic audio file validation and storage operations.
"""

from pathlib import Path

from fastapi import UploadFile

from ..config import settings


ALLOWED_AUDIO_EXTENSIONS = {
    ".wav",
    ".mp3",
    ".flac",
    ".aiff",
    ".aif",
    ".m4a",
}


class AudioService:
    """
    Service responsible for audio file operations.
    """

    def __init__(self) -> None:
        self.upload_dir = Path(settings.upload_dir)
        self.master_dir = Path(settings.master_dir)

        self.upload_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.master_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def is_supported_format(self, filename: str) -> bool:
        """
        Check whether an audio filename uses a supported format.
        """

        extension = Path(filename).suffix.lower()

        return extension in ALLOWED_AUDIO_EXTENSIONS

    def get_upload_path(
        self,
        file_id: str,
        extension: str,
    ) -> Path:
        """
        Return the storage path for an uploaded audio file.
        """

        extension = extension.lower()

        if not extension.startswith("."):
            extension = f".{extension}"

        return self.upload_dir / f"{file_id}{extension}"

    def get_master_path(
        self,
        filename: str,
    ) -> Path:
        """
        Return the storage path for a mastered audio file.
        """

        return self.master_dir / filename

    async def save_upload(
        self,
        file: UploadFile,
        destination: Path,
        max_size_bytes: int,
    ) -> int:
        """
        Save an uploaded audio file safely.

        Returns the total number of bytes written.
        """

        total_size = 0

        try:
            with destination.open("wb") as output:
                while chunk := await file.read(1024 * 1024):
                    total_size += len(chunk)

                    if total_size > max_size_bytes:
                        destination.unlink(missing_ok=True)

                        raise ValueError(
                            "Audio file exceeds the maximum allowed size."
                        )

                    output.write(chunk)

        finally:
            await file.close()

        return total_size

    def find_uploaded_file(
        self,
        file_id: str,
    ) -> Path | None:
        """
        Find an uploaded audio file by its file ID.
        """

        matches = list(
            self.upload_dir.glob(f"{file_id}.*")
        )

        if not matches:
            return None

        return matches[0]

    def file_exists(
        self,
        path: Path,
    ) -> bool:
        """
        Check whether a file exists.
        """

        return path.exists() and path.is_file()


audio_service = AudioService()
