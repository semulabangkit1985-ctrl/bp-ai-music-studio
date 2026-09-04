import json
from pathlib import Path
from sqlalchemy.orm import Session
from .db import SessionLocal
from .models import MasterJob, AudioFile
from .engine.pipeline import master_song

def process_queued():
    db: Session = SessionLocal()
    try:
        jobs = db.query(MasterJob).filter(MasterJob.status == "queued").limit(10).all()
        for job in jobs:
            job.status = "processing"
            db.commit()
            audio = db.get(AudioFile, job.audio_id)
            try:
                output = str(Path(audio.path).with_name(Path(audio.path).stem + "_master.wav"))
                report = master_song(audio.path, output, job.style)
                job.output_path = output
                job.report_json = json.dumps(report)
                job.status = "completed" if report["qc"]["pass"] else "failed"
            except Exception as exc:
                job.status = "failed"
                job.report_json = json.dumps({"error": str(exc)})
            db.commit()
    finally:
        db.close()

if __name__ == "__main__":
    process_queued()
