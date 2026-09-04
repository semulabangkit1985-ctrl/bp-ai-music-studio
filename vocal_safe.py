def vocal_safety_profile(features: dict) -> dict:
    # Conservative protection policy for an original mixed vocal.
    return {
        "protect_vocal": True,
        "pitch_change": False,
        "formant_change": False,
        "time_stretch": False,
        "voice_replacement": False,
        "max_eq_change_db": 1.5,
        "max_vocal_gain_reduction_db": 2.0,
        "deesser_range_db": 2.0,
        "preserve_original_mix": True,
    }
