"""
SONIQ MASTER AI
Vocal Safe processing rules.

Protects the original singer's identity during mastering.
"""


class VocalSafeProcessor:
    """
    Defines safety limits for vocal-preserving mastering.
    """

    def __init__(self) -> None:
        self.protection_enabled = True

    def get_safety_rules(self) -> dict:
        """
        Return vocal preservation rules.
        """

        return {
            "enabled": self.protection_enabled,

            "forbidden_processing": {
                "pitch_shift": True,
                "formant_shift": True,
                "voice_replacement": True,
                "voice_cloning": True,
                "unnecessary_time_stretch": True,
            },

            "allowed_processing": {
                "eq": True,
                "dynamic_eq": True,
                "de_essing": True,
                "light_compression": True,
                "subtle_saturation": True,
                "transparent_limiting": True,
                "level_balancing": True,
            },

            "maximum_vocal_gain_db": 2.0,
            "maximum_compression_db": 2.0,
            "maximum_saturation": 0.10,
        }

    def validate_plan(
        self,
        plan: dict,
    ) -> dict:
        """
        Validate a mastering plan against vocal safety rules.
        """

        rules = self.get_safety_rules()

        if not self.protection_enabled:
            return plan

        vocal_processing = plan.get(
            "vocal_processing",
            {},
        )

        forbidden_keys = [
            "pitch_shift",
            "formant_shift",
            "voice_replacement",
            "voice_cloning",
            "time_stretch",
        ]

        for key in forbidden_keys:
            if vocal_processing.get(key, False):
                vocal_processing[key] = False

        plan["vocal_processing"] = vocal_processing

        plan["vocal_safe"] = True

        plan["max_vocal_gain_db"] = rules[
            "maximum_vocal_gain_db"
        ]

        plan["max_compression_db"] = rules[
            "maximum_compression_db"
        ]

        plan["max_saturation"] = rules[
            "maximum_saturation"
        ]

        return plan


vocal_safe_processor = VocalSafeProcessor()
