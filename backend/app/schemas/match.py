from pydantic import BaseModel
from typing import List


class MatchRequest(BaseModel):
    resume_id: int
    job_id: int


class MatchResponse(BaseModel):
    match_id: int
    match_score: int
    matching_skills: List[str]
    missing_skills: List[str]