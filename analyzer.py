from pathlib import Path
import numpy as np
import soundfile as sf

def analyze_mix(path: str) -> dict:
    data, sr = sf.read(path, always_2d=True)
    x = data.astype(np.float64)
    peak = float(np.max(np.abs(x))) if x.size else 0.0
    rms = float(np.sqrt(np.mean(x*x))) if x.size else 0.0
    crest = peak / max(rms, 1e-12)
    duration = len(x) / sr if sr else 0.0
    return {
        "sample_rate": sr,
        "channels": x.shape[1],
        "duration_sec": round(duration, 3),
        "peak_linear": peak,
        "peak_dbfs": round(20*np.log10(max(peak, 1e-12)), 2),
        "rms_dbfs": round(20*np.log10(max(rms, 1e-12)), 2),
        "crest_factor": round(crest, 3),
        "clipping": bool(peak >= 0.99999),
    }
