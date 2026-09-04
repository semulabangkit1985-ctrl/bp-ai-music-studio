"""
SONIQ MASTER AI
Preset service.

Loads and manages mastering presets.
"""

import json
from pathlib import Path


class PresetService:
    """
    Service responsible for loading and retrieving
    SONIQ MASTER AI mastering presets.
    """

    def __init__(
        self,
        preset_file: str = "presets/presets.json",
    ) -> None:
        self.preset_file = Path(preset_file)

    def load_presets(self) -> list[dict]:
        """
        Load all presets from the preset JSON file.
        """

        if not self.preset_file.exists():
            return []

        try:
            with self.preset_file.open(
                "r",
                encoding="utf-8",
            ) as file:
                data = json.load(file)

        except (json.JSONDecodeError, OSError):
            return []

        if not isinstance(data, list):
            return []

        return data

    def get_preset(
        self,
        preset_id: str,
    ) -> dict | None:
        """
        Retrieve a preset by its ID.
        """

        presets = self.load_presets()

        for preset in presets:
            if preset.get("id") == preset_id:
                return preset

        return None

    def get_all_presets(self) -> list[dict]:
        """
        Return all available mastering presets.
        """

        return self.load_presets()


preset_service = PresetService()
