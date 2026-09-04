"""
SONIQ MASTER AI
Saturation processing module.

Applies subtle harmonic coloration without
damaging vocal clarity or dynamics.
"""

from dataclasses import dataclass


@dataclass
class SaturationSettings:
    """
    Saturation parameters.
    """

    amount: float
    drive_db: float
    mix: float
    enabled: bool


class SaturationProcessor:
    """
    Creates conservative saturation settings.
    """

    def create_settings(
        self,
        preset: str = "universal",
        vocal_safe: bool = True,
    ) -> SaturationSettings:
        """
        Generate saturation settings for the mastering chain.
        """

        amount = 0.05
        drive_db = 1.0
        mix = 0.10

        if preset == "fire":
            amount = 0.10
            drive_db = 1.5
            mix = 0.15

        elif preset == "tape":
            amount = 0.08
            drive_db = 1.2
            mix = 0.12

        elif preset == "natural":
            amount = 0.03
            drive_db = 0.5
            mix = 0.05

        elif preset == "cinematic":
            amount = 0.06
            drive_db = 1.0
            mix = 0.10

        if vocal_safe:
            amount = min(amount, 0.10)
            drive_db = min(drive_db, 1.5)
            mix = min(mix, 0.15)

        return SaturationSettings(
            amount=amount,
            drive_db=drive_db,
            mix=mix,
            enabled=True,
        )

    def to_dict(
        self,
        settings: SaturationSettings,
    ) -> dict:
        """
        Convert saturation settings to a dictionary.
        """

        return {
            "amount": settings.amount,
            "drive_db": settings.drive_db,
            "mix": settings.mix,
            "enabled": settings.enabled,
        }


saturation_processor = SaturationProcessor()
