"""
SONIQ MASTER AI
Audio analysis service.

Provides basic technical analysis of uploaded audio files.
"""

from pathlib import Path

import librosa
import numpy as np
import soundfile as sf


class AnalysisService:
    """
    Service responsible for analyzing audio characteristics.
    """

    def analyze(self, audio_path: Path) -> dict:
        """
        Analyze an audio file and return technical information.
        """

        if not audio_path.exists():
            raise FileNotFoundError(
                f"Audio file not found: {audio_path}"
            )

        data, sample_rate = sf.read(
            str(audio_path),
            always_2d=True,
        )

        if data.size == 0:
            raise ValueError("Audio file contains no samples.")

        channels = data.shape[1]

        mono = np.mean(data, axis=1).astype(np.float32)

        duration = len(mono) / sample_rate

        peak = float(np.max(np.abs(mono)))

        if peak > 0:
            peak_db = float(
                20.0 * np.log10(peak)
            )
        else:
            peak_db = -np.inf

        rms = float(
            np.sqrt(np.mean(np.square(mono)))
        )

        if rms > 0:
            rms_db = float(
                20.0 * np.log10(rms)
            )
        else:
            rms_db = -np.inf

        try:
            tempo, _ = librosa.beat.beat_track(
                y=mono,
                sr=sample_rate,
            )

            tempo_value = float(
                np.asarray(tempo).reshape(-1)[0]
            )

        except Exception:
            tempo_value = None

        return {
            "duration_seconds": round(
                duration,
                3,
            ),
            "sample_rate": int(sample_rate),
            "channels": int(channels),
            "peak_db": round(
                peak_db,
                2,
            ) if np.isfinite(peak_db) else None,
            "rms_db": round(
                rms_db,
                2,
            ) if np.isfinite(rms_db) else None,
            "tempo_bpm": round(
                tempo_value,
                2,
            ) if tempo_value is not None else None,
            "integrated_lufs": None,
            "true_peak_db": None,
            "dynamic_range_db": None,
            "vocal_presence": None,
        }


analysis_service = AnalysisService()
