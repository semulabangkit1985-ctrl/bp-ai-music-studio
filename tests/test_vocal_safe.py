from apps.engine.vocal_safe import vocal_safe_processor


def test_vocal_safe_disables_forbidden_processing():
    plan = {
        "vocal_processing": {
            "pitch_shift": True,
            "formant_shift": True,
            "voice_replacement": True,
            "voice_cloning": True,
            "time_stretch": True,
        }
    }

    result = vocal_safe_processor.validate_plan(plan)

    vocal_processing = result["vocal_processing"]

    assert vocal_processing["pitch_shift"] is False
    assert vocal_processing["formant_shift"] is False
    assert vocal_processing["voice_replacement"] is False
    assert vocal_processing["voice_cloning"] is False
    assert vocal_processing["time_stretch"] is False

    assert result["vocal_safe"] is True
