import numpy as np
import soundfile as sf

from apps.engine.analyzer import analyzer


def test_analyzer_reads_wav(tmp_path):
    audio_path = tmp_path / "test.wav"

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

    result = analyzer.analyze(audio_path)

    assert result["sample_rate"] == 44100
    assert result["channels"] == 1
    assert result["duration_seconds"] > 0
    assert result["peak_db"] is not None
