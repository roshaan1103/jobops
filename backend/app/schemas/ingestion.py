from pydantic import BaseModel
from typing import Optional

class JobIngestionRequest(BaseModel):
    source: str  # "url" | "text" | "linkedin" | "indeed"
    content: str  # url OR pasted text OR job description
    title: Optional[str] = None
    company: Optional[str] = None