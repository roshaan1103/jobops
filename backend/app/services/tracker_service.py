import pandas as pd
import os

FILE_PATH = "job_tracker.xlsx"


def init_tracker():
    """Create Excel file if not exists"""
    if not os.path.exists(FILE_PATH):
        df = pd.DataFrame(columns=[
            "job_id",
            "title",
            "company",
            "role",
            "match_score",
            "resume_pdf",
            "applied",
            "response_status",
            "date_applied"
        ])
        df.to_excel(FILE_PATH, index=False)


def add_job_entry(entry: dict):
    """Append job entry to Excel tracker"""

    init_tracker()

    df = pd.read_excel(FILE_PATH)

    new_row = {
        "job_id": entry.get("job_id"),
        "title": entry.get("title"),
        "company": entry.get("company"),
        "role": entry.get("role"),
        "match_score": entry.get("match_score"),
        "resume_pdf": entry.get("resume_pdf"),
        "applied": entry.get("applied", False),
        "response_status": entry.get("response_status", "not applied"),
        "date_applied": entry.get("date_applied")
    }

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    df.to_excel(FILE_PATH, index=False)


def get_all_jobs():
    init_tracker()
    return pd.read_excel(FILE_PATH)