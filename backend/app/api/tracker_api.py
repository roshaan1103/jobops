from fastapi import APIRouter
from app.services.tracker_service import get_all_jobs

router = APIRouter()


@router.get("/tracker/jobs")
def fetch_jobs():
    df = get_all_jobs()
    return df.to_dict(orient="records")