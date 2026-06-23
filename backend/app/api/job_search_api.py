from fastapi import APIRouter

from app.services.job_search_service import search_jobs

router = APIRouter()


@router.get("/search-jobs")
def search(role: str, experience: int = None):

    results = search_jobs(role, experience)

    return {
        "results": results
    }