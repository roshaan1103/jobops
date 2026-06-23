from app.services.master_profile import (
    get_devops_profile,
    get_cloud_profile
)

from app.services.job_intelligence import analyze_job


def get_profile(profile_type: str):

    profile_type = profile_type.lower()

    if profile_type == "cloud":
        return get_cloud_profile()

    return get_devops_profile()


def calculate_profile_match(
    profile_type: str,
    job_description: str
):

    profile = get_profile(profile_type)

    job_data = analyze_job(job_description)

    profile_skills = set()

    for category in profile["skills"].values():
        profile_skills.update(
            [s.lower() for s in category]
        )

    job_skills = set(
        [s.lower() for s in job_data["skills"]]
    )

    matching = list(
        profile_skills & job_skills
    )

    missing = list(
        job_skills - profile_skills
    )

    if len(job_skills) == 0:
        score = 0
    else:
        score = round(
            (len(matching) / len(job_skills))
            * 100
        )

    return {
        "score": score,
        "matching_skills": matching,
        "missing_skills": missing,
        "profile": profile,
        "job_data": job_data
    }