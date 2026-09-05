"""
SONIQ MASTER AI
Dynamics processing module.

Controls overall dynamics while preserving
transients, punch and vocal expression.
"""

from dataclasses import dataclass


@dataclass
class DynamicsSettings:
    """
    Dynamic processing parameters.
    """

    target_dynamic_range_db: float
    transient_preservation: float
    compression_amount: float
    limiter_amount: float
    preserve_transients: bool


class DynamicsProcessor:
    """
    Creates safe dynamics settings for mastering.
    """

    def create_settings(
        self,
        preset: str = "universal",
        vocal_safe: bool = True,
    ) -> DynamicsSettings:
        """
        Generate dynamics processing settings.
        """

        if vocal_safe:
            target_range = 8.0
            compression = 0.20
            limiter = 0.15
            transient = 0.90
        else:
            target_range = 7.0
            compression = 0.30
            limiter = 0.25
            transient = 0.80

        if preset == "natural":
            target_range = 10.0
            compression = 0.10
            limiter = 0.10
            transient = 0.98

        elif preset == "punch":
            target_range = 8.0
            compression = 0.15
            limiter = 0.20
            transient = 1.00

        elif preset == "fire":
            target_range = 7.0
            compression = 0.25
            limiter = 0.25
            transient = 0.90

        elif preset == "cinematic":
            target_range = 10.0
            compression = 0.15
            limiter = 0.15
            transient = 0.95

        if vocal_safe:
            compression = min(
                compression,
                0.25,
            )

            limiter = min(
                limiter,
                0.20,
            )

            transient = max(
                transient,
                0.90,
            )

        return DynamicsSettings(
            target_dynamic_range_db=target_range,
            transient_preservation=transient,
            compression_amount=compression,
            limiter_amount=limiter,
            preserve_transients=True,
        )

    def to_dict(
        self,
        settings: DynamicsSettings,
    ) -> dict:
        """
        Convert dynamics settings to a dictionary.
        """

        return {
            "target_dynamic_range_db": (
                settings.target_dynamic_range_db
            ),
            "transient_preservation": (
                settings.transient_preservation
            ),
            "compression_amount": (
                settings.compression_amount
            ),
            "limiter_amount": (
                settings.limiter_amount
            ),
            "preserve_transients": (
                settings.preserve_transients
            ),
        }


dynamics_processor = DynamicsProcessor()
