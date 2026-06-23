from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
    ForeignKey
)

from datetime import datetime

from app.db.base import Base


class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)

    resume_id = Column(Integer, nullable=False)
    job_id = Column(Integer, nullable=False)

    match_score = Column(Integer)

    matching_skills = Column(Text)
    missing_skills = Column(Text)

