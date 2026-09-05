"""
SONIQ MASTER AI
Mastering pipeline.

Connects analysis, AI decisions, vocal safety,
processing modules, rendering and quality control.
"""

from pathlib import Path

from .ai_master import ai_master_engine
from .analyzer import analyzer
from .compressor import compressor_processor
from .dynamics import dynamics_processor
from .eq import eq_processor
from .limiter import limiter_processor
from .loudness import loudness_processor
from .qc import quality_control
from .render import renderer
from .saturation import saturation_processor
from .stereo import stereo_processor
from .vocal_safe import vocal_safe_processor


class MasteringPipeline:
    """
    Complete SONIQ MASTER AI processing pipeline.
    """

    def analyze(
        self,
        input_path: str | Path,
    ) -> dict:
        """
        Analyze the source audio.
        """

        return analyzer.analyze(input_path)

    def create_plan(
        self,
        analysis: dict,
        preset: str = "universal",
        target_lufs: float = -14.0,
        true_peak_db: float = -1.0,
        vocal_safe: bool = True,
    ) -> dict:
        """
        Create a safe mastering plan.
        """

        plan = ai_master_engine.create_plan(
            analysis=analysis,
            preset=preset,
            target_lufs=target_lufs,
            true_peak_db=true_peak_db,
            vocal_safe=vocal_safe,
        )

        plan = vocal_safe_processor.validate_plan(
            plan
        )

        plan["eq_bands"] = eq_processor.to_dict(
            eq_processor.create_bands(
                preset=preset,
                vocal_safe=vocal_safe,
            )
        )

        plan["compressor"] = compressor_processor.to_dict(
            compressor_processor.create_settings(
                preset=preset,
                vocal_safe=vocal_safe,
            )
        )

        plan["limiter"] = limiter_processor.to_dict(
            limiter_processor.create_settings(
                true_peak_db=true_peak_db,
                vocal_safe=vocal_safe,
            )
        )

        plan["stereo"] = stereo_processor.to_dict(
            stereo_processor.create_settings(
                preset=preset,
                vocal_safe=vocal_safe,
            )
        )

        plan["saturation"] = saturation_processor.to_dict(
            saturation_processor.create_settings(
                preset=preset,
                vocal_safe=vocal_safe,
            )
        )

        plan["loudness"] = loudness_processor.to_dict(
            loudness_processor.create_settings(
                target_lufs=target_lufs,
                true_peak_db=true_peak_db,
                vocal_safe=vocal_safe,
            )
        )

        plan["dynamics"] = dynamics_processor.to_dict(
            dynamics_processor.create_settings(
                preset=preset,
                vocal_safe=vocal_safe,
            )
        )

        return plan

    def render(
        self,
        input_path: str | Path,
        output_path: str | Path,
        true_peak_db: float = -1.0,
    ) -> Path:
        """
        Render the final audio.
        """

        return renderer.render(
            input_path=input_path,
            output_path=output_path,
            target_peak_db=true_peak_db,
        )

    def run_qc(
        self,
        output_path: str | Path,
        true_peak_db: float = -1.0,
    ) -> dict:
        """
        Run quality control on the final master.
        """

        return quality_control.check(
            audio_path=output_path,
            target_peak_db=true_peak_db,
        )

    def run(
        self,
        input_path: str | Path,
        output_path: str | Path,
        preset: str = "universal",
        target_lufs: float = -14.0,
        true_peak_db: float = -1.0,
        vocal_safe: bool = True,
    ) -> dict:
        """
        Run the complete mastering workflow.

        The current renderer performs the final export stage.
        DSP modules provide the processing plan for the
        production mastering engine.
        """

        analysis = self.analyze(
            input_path
        )

        plan = self.create_plan(
            analysis=analysis,
            preset=preset,
            target_lufs=target_lufs,
            true_peak_db=true_peak_db,
            vocal_safe=vocal_safe,
        )

        rendered_file = self.render(
            input_path=input_path,
            output_path=output_path,
            true_peak_db=true_peak_db,
        )

        qc = self.run_qc(
            output_path=rendered_file,
            true_peak_db=true_peak_db,
        )

        return {
            "status": (
                "completed"
                if qc["passed"]
                else "qc_failed"
            ),
            "analysis": analysis,
            "plan": plan,
            "output_file": str(rendered_file),
            "quality_control": qc,
        }


mastering_pipeline = MasteringPipeline()
