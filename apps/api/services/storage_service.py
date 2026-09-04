"""
SONIQ MASTER AI
Storage service.

Handles audio file storage and path management.
"""

from pathlib import Path

from ..config import settings


class StorageService:
    """
    Service responsible for managing uploaded and
    mastered audio files.
    """

    def __init__(self) -> None:
        self.upload_dir = Path(settings.upload_dir)
        self.master_dir = Path(settings.master_dir)

        self.ensure_directories()

    def ensure_directories(self) -> None:
        """
        Create required storage directories.
        """

        self.upload_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.master_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def upload_path(
        self,
        filename: str,
    ) -> Path:
        """
        Return the path for an uploaded file.
        """

        return self.upload_dir / Path(filename).name

    def master_path(
        self,
        filename: str,
    ) -> Path:
        """
        Return the path for a mastered file.
        """

        return self.master_dir / Path(filename).name

    def exists(
        self,
        path: Path,
    ) -> bool:
        """
        Check whether a stored file exists.
        """

        return path.exists() and path.is_file()

    def delete(
        self,
        path: Path,
    ) -> bool:
        """
        Delete a stored file if it exists.
        """

        if not self.exists(path):
            return False

        path.unlink()

        return True

    def file_size(
        self,
        path: Path,
    ) -> int:
        """
        Return file size in bytes.
        """

        if not self.exists(path):
            return 0

        return path.stat().st_size


storage_service = StorageService()
