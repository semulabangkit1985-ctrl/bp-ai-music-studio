"""
SONIQ MASTER AI
Mastering compressor module.

Provides gentle dynamic control while preserving
the natural character of the original vocal.
"""

from dataclasses import dataclass


@dataclass
class CompressorSettings:
    """
    Compressor parameters for the mastering chain.
    """

    threshold_db: float
    ratio: float
    attack_ms: float
    release_ms: float
    knee_db: float
    makeup_gain_db: float
    max_gain_reduction_db: float


class CompressorProcessor:
    """
    Creates conservative mastering compression settings.
    """

    def create_settings(
        self,
        preset: str = "universal",
        vocal_safe: bool = True,
    ) -> CompressorSettings:
        """
        Generate compressor settings.
        """

        if vocal_safe:
            ratio = 1.5
            threshold = -18.0
            max_reduction = 2.0
        else:
            ratio = 2.0
            threshold = -20.0
            max_reduction = 3.0

        attack = 30.0
        release = 120.0
        knee = 6.0
        makeup_gain = 0.0

        if preset == "punch":
            attack = 40.0
            release = 100.0

        elif preset == "natural":
            ratio = 1.3
            threshold = -16.0
            max_reduction = 1.5

        elif preset == "cinematic":
            attack = 50.0
            release = 180.0

        elif preset == "fire":
            ratio = 1.7
            release = 100.0

        return CompressorSettings(
            threshold_db=threshold,
            ratio=ratio,
            attack_ms=attack,
            release_ms=release,
            knee_db=knee,
            makeup_gain_db=makeup_gain,
            max_gain_reduction_db=max_reduction,
        )

    def to_dict(
        self,
        settings: CompressorSettings,
    ) -> dict:
        """
        Convert compressor settings to a dictionary.
        """

        return {
            "threshold_db": settings.threshold_db,
            "ratio": settings.ratio,
            "attack_ms": settings.attack_ms,
            "release_ms": settings.release_ms,
            "knee_db": settings.knee_db,
            "makeup_gain_db": settings.makeup_gain_db,
            "max_gain_reduction_db": settings.max_gain_reduction_db,
        }


compressor_processor = CompressorProcessor()
