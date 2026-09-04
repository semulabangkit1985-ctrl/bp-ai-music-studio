"""
SONIQ MASTER AI
Transparent mastering limiter.

Controls final peak level while protecting the
natural character of the original vocal.
"""

from dataclasses import dataclass


@dataclass
class LimiterSettings:
    """
    Final limiter parameters.
    """

    ceiling_db: float
    release_ms: float
    lookahead_ms: float
    max_gain_reduction_db: float
    true_peak: bool


class LimiterProcessor:
    """
    Creates safe final limiting settings.
    """

    def create_settings(
        self,
        true_peak_db: float = -1.0,
        vocal_safe: bool = True,
    ) -> LimiterSettings:
        """
        Generate transparent limiter settings.
        """

        ceiling = max(
            -3.0,
            min(true_peak_db, -0.1),
        )

        if vocal_safe:
            max_reduction = 2.0
            release = 100.0
        else:
            max_reduction = 3.0
            release = 80.0

        return LimiterSettings(
            ceiling_db=ceiling,
            release_ms=release,
            lookahead_ms=5.0,
            max_gain_reduction_db=max_reduction,
            true_peak=True,
        )

    def to_dict(
        self,
        settings: LimiterSettings,
    ) -> dict:
        """
        Convert limiter settings to a dictionary.
        """

        return {
            "ceiling_db": settings.ceiling_db,
            "release_ms": settings.release_ms,
            "lookahead_ms": settings.lookahead_ms,
            "max_gain_reduction_db": (
                settings.max_gain_reduction_db
            ),
            "true_peak": settings.true_peak,
        }


limiter_processor = LimiterProcessor()
