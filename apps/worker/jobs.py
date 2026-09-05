"""
SONIQ MASTER AI
Background mastering jobs.

Handles audio mastering tasks outside the API request cycle.
"""

from pathlib import Path

from apps.engine.pipeline import mastering_pipeline


def process_mastering_job(
    input_path: str,
    output_path: str,
    preset: str = "universal",
    target_lufs: float = -14.0,
    true_peak_db: float = -1.0,
    vocal_safe: bool = True,
) -> dict:
    """
    Process one mastering job.
    """

    source = Path(input_path)
    destination = Path(output_path)

    if not source.exists():
        raise FileNotFoundError(
            f"Input audio file not found: {source}"
        )

    destination.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    result = mastering_pipeline.run(
        input_path=source,
        output_path=destination,
        preset=preset,
        target_lufs=target_lufs,
        true_peak_db=true_peak_db,
        vocal_safe=vocal_safe,
    )

    return result


def process_job(payload: dict) -> dict:
    """
    Process a mastering job from a queue payload.
    """

    return process_mastering_job(
        input_path=payload["input_path"],
        output_path=payload["output_path"],
        preset=payload.get(
            "preset",
            "universal",
        ),
        target_lufs=payload.get(
            "target_lufs",
            -14.0,
        ),
        true_peak_db=payload.get(
            "true_peak_db",
            -1.0,
        ),
        vocal_safe=payload.get(
            "vocal_safe",
            True,
        ),
  )
