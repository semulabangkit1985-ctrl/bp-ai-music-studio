STYLES = {
    "Universal": {"low_db": -0.2, "high_db": 0.2, "target_lufs": -11.0},
    "Natural": {"low_db": -0.1, "high_db": 0.1, "target_lufs": -12.0},
    "Clarity": {"low_db": -0.3, "high_db": 0.5, "target_lufs": -11.0},
    "Tape": {"low_db": 0.1, "high_db": -0.1, "target_lufs": -12.0},
    "Punch": {"low_db": -0.2, "high_db": 0.1, "target_lufs": -10.5},
    "Fire": {"low_db": 0.1, "high_db": 0.4, "target_lufs": -10.0},
    "Spatial": {"low_db": -0.2, "high_db": 0.2, "target_lufs": -11.5},
    "Cinematic": {"low_db": -0.1, "high_db": 0.3, "target_lufs": -12.0},
}

def build_mastering_plan(features: dict, style: str, vocal: dict) -> dict:
    preset = STYLES.get(style, STYLES["Natural"])
    plan = dict(preset)
    plan["vocal_safety"] = vocal
    # Adaptive guardrails.
    if features.get("clipping"):
        plan["target_lufs"] = min(plan["target_lufs"], -12.0)
    return plan
