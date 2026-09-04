"""
SONIQ MASTER AI
Audio-related API schemas.
"""

from pydantic import BaseModel, Field


class AudioUploadResponse(BaseModel):
    """
    Response returned after an audio file is uploaded.
    """

    status: str
    file_id: str
    filename: str
    format: str
    size_bytes: int
    path: str


class AudioAnalysis(BaseModel):
    """
    Basic audio analysis information.
    """

    duration_seconds: float | None = None
    sample_rate: int | None = None
    channels: int | None = None
    integrated_lufs: float | None = None
    true_peak_db: float | None = None
    dynamic_range_db: float | None = None
    peak_db: float | None = None
    vocal_presence: float | None = Field(
        default=None,
        ge=0.0,
        le=1.0,
    )


class AudioAnalysisResponse(BaseModel):
    """
    Response returned after audio analysis.
    """

    status: str
    file_id: str
    filename: str
    analysis: AudioAnalysis
