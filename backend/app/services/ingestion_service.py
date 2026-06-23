from sqlalchemy.orm import Session

from app.models.job import Job
from app.services.ingestion_router import route_scraper
from app.services.job_intelligence import analyze_job
import json


def normalize_job(source: str, content: str) -> str:

    if source == "url":
        return route_scraper(content)

    if source in ["text", "linkedin", "indeed"]:
        return content

    return content


def ingest_job(
    db: Session,
    source: str,
    content: str,
    title=None,
    company=None
):

    raw_text = normalize_job(source, content)

    analysis = analyze_job(raw_text)

    job = Job(
        title=title or "Unknown",
        company=company,
        description=analysis["clean_text"],

        # NEW INTELLIGENCE (we temporarily store inside description or JSON if no schema yet)
        # If you later add columns, we move these properly:
        embedding=json.dumps(analysis["embedding"].tolist())
    )

    db.add(job)
    db.commit()
    db.refresh(job)

    return job, analysis