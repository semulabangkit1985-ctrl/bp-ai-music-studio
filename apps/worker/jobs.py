"""
SONIQ MASTER AI
Background worker jobs.

Handles asynchronous audio mastering tasks.
"""

from pathlib import Path

from apps.engine.pipeline import mastering_pipeline


def run_mastering_job(
    input_path: str,
    output_path: str,
    preset: str = "universal",
    target_lufs: float = -14.0,
    true_peak_db: float = -1.0,
    vocal_safe: bool = True,
) -> dict:
    """
    Run a complete mastering job in the background worker.
    """

    input_file = Path(input_path)
    output_file = Path(output_path)

    if not input_file.exists():
        raise FileNotFoundError(
            f"Input audio file not found: {input_file}"
        )

    output_file.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    return mastering_pipeline.run(
        input_path=input_file,
        output_path=output_file,
        preset=preset,
        target_lufs=target_lufs,
        true_peak_db=true_peak_db,
        vocal_safe=vocal_safe,
    )
