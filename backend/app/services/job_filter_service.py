from typing import List

def filter_job_query(role: str, experience: int = None, keywords: List[str] = None):

    query_parts = []

    if role:
        query_parts.append(role)

    if experience:
        query_parts.append(f"{experience} years")

    if keywords:
        query_parts.extend(keywords)

    return " ".join(query_parts)