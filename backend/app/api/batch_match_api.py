from fastapi import APIRouter

from app.services.job_search_service import search_jobs
from app.services.batch_match_service import batch_match_jobs

router = APIRouter()


@router.get("/batch-match")
def batch_match(role: str, experience: int = None):

    jobs = search_jobs(role, experience)

    results = batch_match_jobs(jobs)

    return {
        "count": len(results),
        "top_matches": results[:10]
    }