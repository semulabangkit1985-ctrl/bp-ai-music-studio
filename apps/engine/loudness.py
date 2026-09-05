"""
SONIQ MASTER AI
Loudness processing module.

Controls final loudness targets while preserving
vocal clarity, dynamics and true-peak safety.
"""

from dataclasses import dataclass


@dataclass
class LoudnessSettings:
    """
    Loudness parameters.
    """

    target_lufs: float
    max_true_peak_db: float
    tolerance_lufs: float
    enabled: bool


class LoudnessProcessor:
    """
    Creates conservative loudness settings
    for the mastering chain.
    """

    def create_settings(
        self,
        preset: str = "universal",
        vocal_safe: bool = True,
    ) -> LoudnessSettings:
        """
        Generate loudness settings for the mastering chain.
        """

        # Conservative universal mastering target.
        target_lufs = -14.0
        max_true_peak_db = -1.0
        tolerance_lufs = 0.5

        if preset == "fire":
            target_lufs = -9.0
            max_true_peak_db = -1.0
            tolerance_lufs = 0.5

        elif preset == "tape":
            target_lufs = -12.0
            max_true_peak_db = -1.0
            tolerance_lufs = 0.5

        elif preset == "natural":
            target_lufs = -14.0
            max_true_peak_db = -1.0
            tolerance_lufs = 0.5

        elif preset == "cinematic":
            target_lufs = -16.0
            max_true_peak_db = -1.0
            tolerance_lufs = 0.5

        # Protect vocals and preserve reasonable dynamics.
        if vocal_safe:
            target_lufs = max(target_lufs, -14.0)
            max_true_peak_db = min(max_true_peak_db, -1.0)
            tolerance_lufs = max(tolerance_lufs, 0.5)

        return LoudnessSettings(
            target_lufs=target_lufs,
            max_true_peak_db=max_true_peak_db,
            tolerance_lufs=tolerance_lufs,
            enabled=True,
        )

    def to_dict(
        self,
        settings: LoudnessSettings,
    ) -> dict:
        """
        Convert loudness settings to a dictionary.
        """

        return {
            "target_lufs": settings.target_lufs,
            "max_true_peak_db": settings.max_true_peak_db,
            "tolerance_lufs": settings.tolerance_lufs,
            "enabled": settings.enabled,
        }


loudness_processor = LoudnessProcessor()
