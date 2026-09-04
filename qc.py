import soundfile as sf
import numpy as np

def run_qc(path: str) -> dict:
    x, _ = sf.read(path, always_2d=True)
    peak = float(np.max(np.abs(x))) if x.size else 0.0
    return {
        "pass": bool(np.isfinite(x).all() and peak < 1.0),
        "peak_linear": peak,
        "clipping": bool(peak >= 1.0),
    }
