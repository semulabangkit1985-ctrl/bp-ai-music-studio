"""
SONIQ MASTER AI
Loudness control module.

Controls mastering loudness while protecting
the natural dynamics and vocal clarity.
"""

from dataclasses import dataclass


@dataclass
class LoudnessSettings:
    """
    Loudness target parameters.
    """

    target_lufs: float
    true_peak_db: float
    max_gain_db: float
    max_loudness_boost_db: float
    preserve_dynamics: bool


class LoudnessProcessor:
    """
    Creates safe loudness targets for mastering.
    """

    def create_settings(
        self,
        target_lufs: float = -14.0,
        true_peak_db: float = -1.0,
        vocal_safe: bool = True,
    ) -> LoudnessSettings:
        """
        Generate loudness processing settings.
        """

        target = max(
            -24.0,
            min(target_lufs, -5.0),
        )

        ceiling = max(
            -3.0,
            min(true_peak_db, -0.1),
        )

        if vocal_safe:
            max_gain = 6.0
            max_boost = 4.0
        else:
            max_gain = 8.0
            max_boost = 6.0

        return LoudnessSettings(
            target_lufs=target,
            true_peak_db=ceiling,
            max_gain_db=max_gain,
            max_loudness_boost_db=max_boost,
            preserve_dynamics=True,
        )

    def calculate_gain(
        self,
        current_lufs: float,
        settings: LoudnessSettings,
    ) -> float:
        """
        Calculate the required loudness gain.

        The result is limited to avoid excessive processing.
        """

        if current_lufs is None:
            return 0.0

        gain = (
            settings.target_lufs - current_lufs
        )

        gain = max(
            -settings.max_gain_db,
            min(
                gain,
                settings.max_gain_db,
            ),
        )

        gain = max(
            -settings.max_loudness_boost_db,
            min(
                gain,
                settings.max_loudness_boost_db,
            ),
        )

        return round(gain, 2)

    def to_dict(
        self,
        settings: LoudnessSettings,
    ) -> dict:
        """
        Convert loudness settings to a dictionary.
        """

        return {
            "target_lufs": settings.target_lufs,
            "true_peak_db": settings.true_peak_db,
            "max_gain_db": settings.max_gain_db,
            "max_loudness_boost_db": (
                settings.max_loudness_boost_db
            ),
            "preserve_dynamics": (
                settings.preserve_dynamics
            ),
        }


loudness_processor = LoudnessProcessor()
