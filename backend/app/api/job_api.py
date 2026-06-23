from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.job import Job

router = APIRouter()


@router.post("/job")
def create_job(job: dict, db: Session = Depends(get_db)):

    required_fields = ["title", "description"]

    for field in required_fields:
        if not job.get(field):
            return {"error": f"{field} is required"}

    new_job = Job(
        title=job.get("title"),
        company=job.get("company"),
        description=job.get("description"),
        location=job.get("location"),
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return {
        "job_id": new_job.id,
        "status": "created"
    }

@router.get("/jobs")
def get_jobs(db: Session = Depends(get_db)):

    jobs = db.query(Job).all()

    return jobs

