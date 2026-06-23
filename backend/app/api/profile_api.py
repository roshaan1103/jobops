from fastapi import APIRouter

from app.services.profile_service import (
    load_master_profile
)

router = APIRouter()


@router.get("/profile")
def get_profile():

    return load_master_profile()