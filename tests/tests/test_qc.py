import numpy as np
import soundfile as sf

from apps.engine.qc import quality_control


def test_quality_control_passes_valid_audio(tmp_path):
    audio_path = tmp_path / "master.wav"

    sample_rate = 44100
    duration = 1.0

    t = np.linspace(
        0,
        duration,
        sample_rate,
        endpoint=False,
    )

    audio = 0.2 * np.sin(2 * np.pi * 440 * t)

    sf.write(
        audio_path,
        audio,
        sample_rate,
    )

    result = quality_control.check(
        audio_path,
        target_peak_db=-1.0,
    )

    assert result["passed"] is True
    assert result["sample_rate"] == 44100
    assert result["peak_db"] is not None
    assert result["errors"] == []
