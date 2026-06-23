import re


def parse_ats_text(text: str):

    def extract(section):
        match = re.search(
            rf"{section}:(.*?)(?=\n[A-Z]|$)",
            text,
            re.DOTALL
        )
        return match.group(1).strip().split("\n") if match else []

    return {
        "summary": extract("Summary"),
        "skills": extract("Skills"),
        "experience": extract("Experience"),
        "projects": extract("Projects"),
        "education": extract("Education"),
        "certifications": extract("Certifications")
    }