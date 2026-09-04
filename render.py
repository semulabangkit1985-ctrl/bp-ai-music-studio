import subprocess
from pathlib import Path

def render(input_path: str, output_path: str, plan: dict):
    low = plan.get("low_db", 0.0)
    high = plan.get("high_db", 0.0)
    # MVP renderer: gentle tone adjustment + loudness normalization.
    af = (
        f"bass=g={low}:f=120,"
        f"treble=g={high}:f=8000,"
        f"loudnorm=I={plan.get('target_lufs', -12.0)}:TP=-1.0:LRA=11"
    )
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([
        "ffmpeg", "-y", "-i", input_path,
        "-af", af, "-ar", "48000", "-c:a", "pcm_s24le", output_path
    ], check=True, capture_output=True)
    return output_path
