"""
SONIQ MASTER AI
Mastering preset routes.
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/presets",
    tags=["Mastering Presets"],
)


DEFAULT_PRESETS = [
    {
        "id": "universal",
        "name": "Universal",
        "description": "Balanced and neutral mastering.",
    },
    {
        "id": "fire",
        "name": "Fire",
        "description": "Energetic mastering with subtle saturation.",
    },
    {
        "id": "clarity",
        "name": "Clarity",
        "description": "Clean and detailed sound.",
    },
    {
        "id": "tape",
        "name": "Tape",
        "description": "Warm analog-style character.",
    },
    {
        "id": "natural",
        "name": "Natural",
        "description": "Preserves the original character.",
    },
    {
        "id": "spatial",
        "name": "Spatial",
        "description": "Wider stereo presentation.",
    },
    {
        "id": "cinematic",
        "name": "Cinematic",
        "description": "Deep and immersive sound.",
    },
    {
        "id": "punch",
        "name": "Punch",
        "description": "Stronger transient impact.",
    },
]


@router.get("/")
async def get_presets():
    """
    Return available mastering presets.
    """

    return {
        "status": "success",
        "presets": DEFAULT_PRESETS,
    }


@router.get("/{preset_id}")
async def get_preset(preset_id: str):
    """
    Return a single mastering preset.
    """

    for preset in DEFAULT_PRESETS:
        if preset["id"] == preset_id:
            return {
                "status": "success",
                "preset": preset,
            }

    return {
        "status": "not_found",
        "preset": None,
    }
