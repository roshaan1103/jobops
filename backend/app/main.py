from contextlib import asynccontextmanager

from fastapi import FastAPI

from pydantic import BaseModel

from app.db.init_db import init_db

from app.services.job_intelligence import (extract_skills,analyze_job)

from app.api.job_api import (router as job_router)

from app.api.match_api import (router as match_router)

from app.api.resume_generate_api import (router as resume_generate_router)

from app.api.ingestion_api import (router as ingestion_router)

from app.services.profile_service import (load_master_profile)
from app.api.profile_api import (router as profile_router)

from app.api.tracker_api import router as tracker_router

from app.api.job_search_api import router as search_router
from app.api.batch_match_api import router as batch_router

@asynccontextmanager
async def lifespan(app):

    init_db()

    load_master_profile()

    yield


app = FastAPI(
    lifespan=lifespan
)


app.include_router(job_router)
app.include_router(match_router)
app.include_router(resume_generate_router)
app.include_router(ingestion_router)
app.include_router(tracker_router)
app.include_router(profile_router)
app.include_router(search_router)
app.include_router(batch_router)

class JobInput(BaseModel):
    title: str
    description: str




@app.get("/")
def root():

    return {
        "message": "JobOps AI Running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }




@app.post("/job/analyze")
def analyze_job_endpoint(job: JobInput):

    return analyze_job(
        job.description
    )
# for github desktop