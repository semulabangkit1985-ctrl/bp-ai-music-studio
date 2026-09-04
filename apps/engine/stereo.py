"""
SONIQ MASTER AI
Stereo processing module.

Controls stereo width conservatively to maintain
mono compatibility and vocal stability.
"""

from dataclasses import dataclass


@dataclass
class StereoSettings:
    """
    Stereo processing parameters.
    """

    width: float
    low_frequency_mono_hz: float
    max_width: float
    mono_compatible: bool


class StereoProcessor:
    """
    Creates safe stereo mastering settings.
    """

    def create_settings(
        self,
        preset: str = "universal",
        vocal_safe: bool = True,
    ) -> StereoSettings:
        """
        Generate stereo width settings.
        """

        width = 1.0
        max_width = 1.05

        if preset == "spatial":
            width = 1.05
            max_width = 1.10

        elif preset == "cinematic":
            width = 1.04
            max_width = 1.08

        elif preset == "natural":
            width = 1.0
            max_width = 1.02

        elif preset == "punch":
            width = 1.02
            max_width = 1.05

        if vocal_safe:
            width = min(width, 1.05)
            max_width = min(max_width, 1.10)

        return StereoSettings(
            width=width,
            low_frequency_mono_hz=120.0,
            max_width=max_width,
            mono_compatible=True,
        )

    def to_dict(
        self,
        settings: StereoSettings,
    ) -> dict:
        """
        Convert stereo settings to a dictionary.
        """

        return {
            "width": settings.width,
            "low_frequency_mono_hz": (
                settings.low_frequency_mono_hz
            ),
            "max_width": settings.max_width,
            "mono_compatible": settings.mono_compatible,
        }


stereo_processor = StereoProcessor()
