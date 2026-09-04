from .analyzer import analyze_mix
from .vocal_safe import vocal_safety_profile
from .ai_master import build_mastering_plan
from .render import render
from .qc import run_qc

def master_song(input_path: str, output_path: str, style: str):
    features = analyze_mix(input_path)
    vocal = vocal_safety_profile(features)
    plan = build_mastering_plan(features, style, vocal)
    render(input_path, output_path, plan)
    qc = run_qc(output_path)
    return {"analysis": features, "vocal_safety": vocal, "plan": plan, "qc": qc}
