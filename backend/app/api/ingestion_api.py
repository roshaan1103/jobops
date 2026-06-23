from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.ingestion import JobIngestionRequest
from app.services.ingestion_service import ingest_job
from app.db.session import get_db

router = APIRouter()


@router.post("/ingest/job")
def ingest_job_endpoint(
    payload: JobIngestionRequest,
    db: Session = Depends(get_db)
):

    job = ingest_job(
        db=db,
        source=payload.source,
        content=payload.content,
        title=payload.title,
        company=None
    )

    return {
        "job_id": job.id,
        "status": "ingested"
    }