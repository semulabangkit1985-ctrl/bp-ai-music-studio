"""
SONIQ MASTER AI
Quality control module.

Checks the final master for technical problems
before it is delivered to the user.
"""

from pathlib import Path

import numpy as np
import soundfile as sf


class QualityControl:
    """
    Performs basic quality checks on mastered audio.
    """

    def check(
        self,
        audio_path: str | Path,
        target_peak_db: float = -1.0,
    ) -> dict:
        """
        Run quality control checks.
        """

        path = Path(audio_path)

        if not path.exists():
            raise FileNotFoundError(
                f"Master file not found: {path}"
            )

        audio, sample_rate = sf.read(
            str(path),
            always_2d=True,
        )

        if audio.size == 0:
            return {
                "passed": False,
                "errors": ["Audio file is empty."],
                "warnings": [],
            }

        peak = float(
            np.max(np.abs(audio))
        )

        peak_db = (
            20.0 * np.log10(peak)
            if peak > 0
            else -np.inf
        )

        errors = []
        warnings = []

        if not np.isfinite(peak_db):
            errors.append(
                "Unable to determine audio peak."
            )

        elif peak_db > target_peak_db + 0.1:
            errors.append(
                "Peak level exceeds the configured ceiling."
            )

        if np.any(np.isnan(audio)):
            errors.append(
                "Audio contains NaN samples."
            )

        if np.any(np.isinf(audio)):
            errors.append(
                "Audio contains infinite samples."
            )

        if sample_rate < 44100:
            warnings.append(
                "Sample rate is below 44.1 kHz."
            )

        passed = len(errors) == 0

        return {
            "passed": passed,
            "sample_rate": int(sample_rate),
            "peak_db": (
                round(peak_db, 2)
                if np.isfinite(peak_db)
                else None
            ),
            "target_peak_db": target_peak_db,
            "errors": errors,
            "warnings": warnings,
        }


quality_control = QualityControl()
