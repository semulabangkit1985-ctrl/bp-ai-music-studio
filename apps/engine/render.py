"""
SONIQ MASTER AI
Audio rendering module.

Renders the final mastered audio while preserving
the original audio character.
"""

from pathlib import Path
import subprocess


class AudioRenderer:
    """
    Handles final audio rendering and export.
    """

    def render(
        self,
        input_path: str | Path,
        output_path: str | Path,
        target_peak_db: float = -1.0,
    ) -> Path:
        """
        Render an audio file to WAV format.

        Uses FFmpeg for the final export stage.
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

        command = [
            "ffmpeg",
            "-y",
            "-i",
            str(source),
            "-af",
            (
                f"alimiter="
                f"limit={10 ** (target_peak_db / 20):.6f}:"
                "level=false"
            ),
            "-ar",
            "44100",
            "-c:a",
            "pcm_s24le",
            str(destination),
        ]

        try:
            subprocess.run(
                command,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )

        except subprocess.CalledProcessError as exc:
            raise RuntimeError(
                "Audio rendering failed."
            ) from exc

        return destination

    def output_exists(
        self,
        output_path: str | Path,
    ) -> bool:
        """
        Check whether the rendered master exists.
        """

        path = Path(output_path)

        return path.exists() and path.is_file()


renderer = AudioRenderer()
