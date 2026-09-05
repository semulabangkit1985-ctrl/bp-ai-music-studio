"""
SONIQ MASTER AI
Engine preset definitions.

Provides the internal mastering profiles used by
the AI mastering pipeline.
"""

PRESETS = {
    "universal": {
        "name": "Universal",
        "description": "Balanced and neutral mastering.",
        "eq": {
            "low_db": 0.0,
            "mid_db": 0.0,
            "high_db": 0.0,
        },
        "compression": 0.20,
        "saturation": 0.05,
        "stereo_width": 1.00,
    },

    "fire": {
        "name": "Fire",
        "description": "Energetic sound with subtle harmonic warmth.",
        "eq": {
            "low_db": 0.5,
            "mid_db": 0.0,
            "high_db": 0.5,
        },
        "compression": 0.25,
        "saturation": 0.10,
        "stereo_width": 1.02,
    },

    "clarity": {
        "name": "Clarity",
        "description": "Clean and detailed presentation.",
        "eq": {
            "low_db": -0.5,
            "mid_db": 0.3,
            "high_db": 0.8,
        },
        "compression": 0.20,
        "saturation": 0.04,
        "stereo_width": 1.02,
    },

    "tape": {
        "name": "Tape",
        "description": "Warm analog-style character.",
        "eq": {
            "low_db": 0.3,
            "mid_db": 0.0,
            "high_db": -0.2,
        },
        "compression": 0.20,
        "saturation": 0.08,
        "stereo_width": 1.00,
    },

    "natural": {
        "name": "Natural",
        "description": "Maximum preservation of the original character.",
        "eq": {
            "low_db": 0.0,
            "mid_db": 0.0,
            "high_db": 0.0,
        },
        "compression": 0.10,
        "saturation": 0.03,
        "stereo_width": 1.00,
    },

    "spatial": {
        "name": "Spatial",
        "description": "Wider stereo presentation.",
        "eq": {
            "low_db": 0.0,
            "mid_db": 0.0,
            "high_db": 0.2,
        },
        "compression": 0.20,
        "saturation": 0.05,
        "stereo_width": 1.05,
    },

    "cinematic": {
        "name": "Cinematic",
        "description": "Deep and immersive mastering.",
        "eq": {
            "low_db": 0.5,
            "mid_db": -0.2,
            "high_db": 0.2,
        },
        "compression": 0.15,
        "saturation": 0.06,
        "stereo_width": 1.04,
    },

    "punch": {
        "name": "Punch",
        "description": "Stronger transient impact.",
        "eq": {
            "low_db": 0.5,
            "mid_db": 0.0,
            "high_db": 0.3,
        },
        "compression": 0.15,
        "saturation": 0.05,
        "stereo_width": 1.02,
    },
}


def get_preset(preset_id: str) -> dict | None:
    """
    Return one mastering preset.
    """

    return PRESETS.get(preset_id)


def get_all_presets() -> list[dict]:
    """
    Return all available mastering presets.
    """

    return [
        {
            "id": preset_id,
            **preset,
        }
        for preset_id, preset in PRESETS.items()
    ]
