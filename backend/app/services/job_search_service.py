from app.services.job_filter_service import filter_job_query
from app.services.job_intelligence import analyze_job


def search_jobs(
    role: str,
    experience: int = None,
    keywords=None
):

    query = filter_job_query(
        role,
        experience,
        keywords
    )

    # Temporary fake jobs
    fake_jobs = [

        {
            "title": f"{role} Engineer",
            "company": "Tech Corp",
            "location": "Remote",
            "description":
                "AWS Kubernetes CI/CD Docker Terraform DevSecOps"
        },

        {
            "title": f"Junior {role}",
            "company": "Cloud Systems Ltd",
            "location": "Remote",
            "description":
                "AWS CloudWatch IAM Linux Terraform"
        },

        {
            "title": f"Senior {role}",
            "company": "Enterprise Inc",
            "location": "Remote",
            "description":
                "Kubernetes Prometheus Grafana AWS Security"
        }

    ]

    results = []

    for job in fake_jobs:

        analysis = analyze_job(
            job["description"]
        )

        results.append({

            "title":
                job["title"],

            "company":
                job["company"],

            "location":
                job["location"],

            "description":
                job["description"],

            "detected_role":
                analysis.get("role"),

            "skills":
                analysis.get("skills"),

            "seniority":
                analysis.get("seniority")

        })

    return results