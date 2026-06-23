from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse
import os
from app.db.session import get_db
from app.models.resume import Resume
from app.models.job import Job
from app.services.ats_generator import generate_ats_resume
from app.services.pdf_generator import create_resume_pdf
from app.services.ats_parser import parse_ats_text

router = APIRouter()


@router.post("/generate-resume/{resume_id}/{job_id}")
def generate(resume_id: int, job_id: int, db: Session = Depends(get_db)):

    resume = db.query(Resume).filter(Resume.id == resume_id).first()
    job = db.query(Job).filter(Job.id == job_id).first()

    if not resume:
        return {"error": "resume not found"}

    if not job:
        return {"error": "job not found"}

    result = generate_ats_resume(resume.content, job.description)

    return {
        "resume_id": resume_id,
        "job_id": job_id,
        "generated_resume": result["generated_resume"],
        "prompt_used": result["prompt"]
    }

@router.post("/resume/pdf")
def create_pdf(ats_text: str):

    structured = parse_ats_text(ats_text)

    file_path = create_resume_pdf(structured)

    return FileResponse(
        file_path,
        media_type="application/pdf",
        filename="ats_resume.pdf"
    )

@router.get("/resume/download/{filename}")
def download_resume(filename: str):
    PDF_DIR = "storage/pdfs"

    file_path = os.path.join(
        PDF_DIR,
        filename
    )

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(
        path=file_path,
        media_type="application/pdf",
        filename=filename
    )