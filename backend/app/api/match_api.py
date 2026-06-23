from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db

from app.models.job import Job

from app.services.profile_matcher import (
    calculate_profile_match
)

from app.services.ats_generator import (
    generate_ats_resume,
    generate_cover_letter
)

from app.services.pdf_generator import (
    create_resume_pdf
)

from app.services.master_profile import get_master_profile
router = APIRouter()


@router.post("/match")
def create_match(
    job_id: int,
    profile_type: str = "devops",
    db: Session = Depends(get_db)
):

    job = (
        db.query(Job)
        .filter(Job.id == job_id)
        .first()
    )

    if not job:
        return {
            "error": "job not found"
        }

    result = calculate_profile_match(
        profile_type,
        job.description
    )

    ats_resume = generate_ats_resume(
        result["profile"],
        job.description
    )

    resume_pdf = create_resume_pdf(
        ats_resume,
        profile,
        filename=f"job_{job.id}.pdf"
    )

    cover_letter = generate_cover_letter(
        result["profile"],
        job.description
    )

    pdf_path = create_resume_pdf(
        ats_resume
    )

    return {

        "job_id": job.id,

        "profile_type": profile_type,

        "match_score":
            result["score"],

        "matching_skills":
            result["matching_skills"],

        "missing_skills":
            result["missing_skills"],

        "role":
            result["job_data"]["role"],

        "experience":
            result["job_data"]["experience"],

        "education":
            result["job_data"]["education"],

        "ats_resume":
            ats_resume,

        "cover_letter":
            cover_letter,

        "resume_pdf":
            pdf_path
    }