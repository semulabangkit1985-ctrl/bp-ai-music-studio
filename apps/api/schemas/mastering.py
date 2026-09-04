"""
SONIQ MASTER AI
Mastering-related API schemas.
"""

from pydantic import BaseModel, Field


class MasteringRequest(BaseModel):
    """
    Request to start an AI mastering job.
    """

    file_id: str = Field(..., min_length=1)
    preset: str = "universal"

    target_lufs: float = Field(
        default=-14.0,
        ge=-24.0,
        le=-5.0,
    )

    true_peak_db: float = Field(
        default=-1.0,
        ge=-3.0,
        le=-0.1,
    )

    vocal_safe: bool = True


class MasteringResponse(BaseModel):
    """
    Response returned when a mastering job is created.
    """

    status: str
    job_id: str
    file_id: str
    preset: str
    target_lufs: float
    true_peak_db: float
    vocal_safe: bool
    message: str


class MasteringStatus(BaseModel):
    """
    Status information for a mastering job.
    """

    job_id: str
    file_id: str
    status: str
    progress: float = Field(
        default=0.0,
        ge=0.0,
        le=100.0,
    )

    output_file: str | None = None
    error: str | None = None
