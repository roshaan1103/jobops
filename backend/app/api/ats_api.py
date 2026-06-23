from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.resume import Resume
from app.models.job import Job

from app.services.ats_generator import (
    generate_ats_resume,
    generate_cover_letter
)

router = APIRouter()


@router.post("/ats/generate/{resume_id}/{job_id}")
def generate_ats(resume_id: int, job_id: int, db: Session = Depends(get_db)):

    resume = db.query(Resume).filter(Resume.id == resume_id).first()
    job = db.query(Job).filter(Job.id == job_id).first()

    if not resume or not job:
        return {"error": "missing data"}

    ats_resume = generate_ats_resume(resume.content, job.description)
    cover_letter = generate_cover_letter(resume.content, job.description)

    return {
        "ats_resume": ats_resume,
        "cover_letter": cover_letter
    }