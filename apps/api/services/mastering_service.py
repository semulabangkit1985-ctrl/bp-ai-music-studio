"""
SONIQ MASTER AI
Mastering service.

Coordinates the AI mastering workflow while keeping
vocal preservation as a core safety requirement.
"""

from pathlib import Path

from ..config import settings
from ..exceptions import MasteringError


class MasteringService:
    """
    Service responsible for starting and managing
    audio mastering jobs.
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

    def validate_input(
        self,
        file_id: str,
    ) -> Path:
        """
        Validate that the requested audio file exists.
        """

        matches = list(
            self.upload_dir.glob(f"{file_id}.*")
        )

        if not matches:
            raise MasteringError(
                "Audio file for mastering was not found."
            )

        return matches[0]

    def create_job(
        self,
        file_id: str,
        preset: str = "universal",
        target_lufs: float = -14.0,
        true_peak_db: float = -1.0,
        vocal_safe: bool = True,
    ) -> dict:
        """
        Create a mastering job description.

        The actual DSP processing is handled by the
        mastering engine and worker layer.
        """

        input_file = self.validate_input(file_id)

        return {
            "status": "queued",
            "file_id": file_id,
            "input_file": str(input_file),
            "preset": preset,
            "target_lufs": target_lufs,
            "true_peak_db": true_peak_db,
            "vocal_safe": vocal_safe,
            "progress": 0.0,
        }

    def get_master_path(
        self,
        filename: str,
    ) -> Path:
        """
        Return the output path for a mastered file.
        """

        return self.master_dir / filename


mastering_service = MasteringService()
