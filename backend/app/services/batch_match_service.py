from app.services.profile_service import load_master_profile
from app.services.job_intelligence import analyze_job


def batch_match_jobs(jobs):

    profile = load_master_profile()

    profile_skills = set()
    for category in profile["skills"].values():
        profile_skills.update(category)

    results = []

    for job in jobs:

        job_data = analyze_job(job["description"])

        job_skills = set(job_data["skills"])

        matching = list(profile_skills & job_skills)

        score = 0
        if job_skills:
            score = round(len(matching) / len(job_skills) * 100)

        results.append({
            "job": job,
            "score": score,
            "matching_skills": matching
        })

    return sorted(results, key=lambda x: x["score"], reverse=True)