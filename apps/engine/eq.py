"""
SONIQ MASTER AI
Equalizer processing module.

Provides safe EQ parameters for mastering.
"""

from dataclasses import dataclass


@dataclass
class EQBand:
    """
    Represents one mastering EQ band.
    """

    frequency_hz: float
    gain_db: float
    q: float
    filter_type: str


class EQProcessor:
    """
    Generates conservative mastering EQ settings.
    """

    def create_bands(
        self,
        preset: str = "universal",
        vocal_safe: bool = True,
    ) -> list[EQBand]:
        """
        Create EQ bands based on the selected preset.
        """

        presets = {
            "universal": {
                "low": 0.0,
                "mid": 0.0,
                "high": 0.0,
            },
            "natural": {
                "low": 0.0,
                "mid": 0.0,
                "high": 0.0,
            },
            "clarity": {
                "low": -0.5,
                "mid": 0.3,
                "high": 0.8,
            },
            "fire": {
                "low": 0.5,
                "mid": 0.0,
                "high": 0.5,
            },
            "tape": {
                "low": 0.3,
                "mid": 0.0,
                "high": -0.2,
            },
            "spatial": {
                "low": 0.0,
                "mid": 0.0,
                "high": 0.2,
            },
            "cinematic": {
                "low": 0.5,
                "mid": -0.2,
                "high": 0.2,
            },
            "punch": {
                "low": 0.5,
                "mid": 0.0,
                "high": 0.3,
            },
        }

        values = presets.get(
            preset,
            presets["universal"],
        )

        # Vocal-safe mode keeps the important
        # vocal presence region conservative.
        mid_gain = values["mid"]

        if vocal_safe:
            mid_gain = max(
                -1.0,
                min(mid_gain, 1.0),
            )

        return [
            EQBand(
                frequency_hz=80.0,
                gain_db=values["low"],
                q=0.70,
                filter_type="low_shelf",
            ),
            EQBand(
                frequency_hz=2500.0,
                gain_db=mid_gain,
                q=0.80,
                filter_type="bell",
            ),
            EQBand(
                frequency_hz=10000.0,
                gain_db=values["high"],
                q=0.70,
                filter_type="high_shelf",
            ),
        ]

    def to_dict(
        self,
        bands: list[EQBand],
    ) -> list[dict]:
        """
        Convert EQ bands to serializable dictionaries.
        """

        return [
            {
                "frequency_hz": band.frequency_hz,
                "gain_db": band.gain_db,
                "q": band.q,
                "filter_type": band.filter_type,
            }
            for band in bands
        ]


eq_processor = EQProcessor()
