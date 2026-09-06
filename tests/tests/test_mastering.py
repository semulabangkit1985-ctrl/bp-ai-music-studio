from apps.engine.ai_master import ai_master_engine
from apps.engine.vocal_safe import vocal_safe_processor


def test_ai_master_creates_safe_plan():
    analysis = {
        "peak_db": -3.0,
        "rms_db": -18.0,
    }

    plan = ai_master_engine.create_plan(
        analysis=analysis,
        preset="universal",
        target_lufs=-14.0,
        true_peak_db=-1.0,
        vocal_safe=True,
    )

    plan = vocal_safe_processor.validate_plan(plan)

    assert plan["preset"] == "universal"
    assert plan["target_lufs"] == -14.0
    assert plan["true_peak_db"] == -1.0
    assert plan["vocal_safe"] is True

    assert plan["vocal_processing"]["pitch_shift"] is False
    assert plan["vocal_processing"]["formant_shift"] is False
    assert plan["vocal_processing"]["voice_cloning"] is False

    assert "eq_bands" not in plan or isinstance(
        plan.get("eq_bands"),
        list,
    )
