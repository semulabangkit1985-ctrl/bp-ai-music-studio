"""
SONIQ MASTER AI
Custom API exceptions.
"""

from fastapi import HTTPException, status


class AudioProcessingError(HTTPException):
    """
    Error raised when audio processing fails.
    """

    def __init__(self, detail: str = "Audio processing failed."):
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=detail,
        )


class AudioFileNotFoundError(HTTPException):
    """
    Error raised when an audio file cannot be found.
    """

    def __init__(self, detail: str = "Audio file not found."):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=detail,
        )


class MasteringError(HTTPException):
    """
    Error raised when mastering fails.
    """

    def __init__(self, detail: str = "Mastering process failed."):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail,
        )
