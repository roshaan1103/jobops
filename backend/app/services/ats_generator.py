from app.services.job_intelligence import analyze_job
import requests
import json


# ------------------------
# PROFILE HELPERS
# ------------------------

def flatten_profile_skills(profile):

    skills = []

    for category in profile["skills"].values():
        skills.extend(category)

    return skills


def format_projects(profile):

    result = []

    for project in profile["projects"]:

        result.append({
            "title": project["title"],
            "tech_stack": project["tech_stack"],
            "bullets": project["bullets"]
        })

    return result


def format_experience(profile):

    return profile["experience"]


def format_education(profile):

    return profile["education"]


# ------------------------
# ATS PROMPT
# ------------------------

def build_ats_prompt(
    profile,
    job_text
):

    job_data = analyze_job(job_text)

    return f"""
You are an expert ATS resume writer.

Generate ONLY valid JSON.

NO markdown.

NO explanations.

NO text outside JSON.

Use ONLY information supplied.

Do NOT invent jobs.

Do NOT invent projects.

JOB ROLE:
{job_data['role']}

JOB SKILLS:
{", ".join(job_data['skills'])}

MASTER PROFILE:

{json.dumps(profile, indent=2)}

OUTPUT FORMAT:

{{
  "summary": "...",

  "skills": [
      "..."
  ],

  "experience": [
      {{
          "role": "...",
          "company": "...",
          "bullets": [
              "..."
          ]
      }}
  ],

  "projects": [
      {{
          "title": "...",
          "tech_stack": [
              "..."
          ],
          "bullets": [
              "..."
          ]
      }}
  ],

  "education": [
      {{
          "degree": "...",
          "institution": "..."
      }}
  ]
}}
"""


# ------------------------
# COVER LETTER
# ------------------------

def build_cover_letter_prompt(
    profile,
    job_text
):

    job_data = analyze_job(job_text)

    profile_skills = flatten_profile_skills(
        profile
    )

    return f"""
Write a professional cover letter.

JOB ROLE:
{job_data['role']}

JOB SKILLS:
{", ".join(job_data['skills'])}

CANDIDATE SKILLS:
{", ".join(profile_skills)}

3-5 paragraphs.

Human sounding.

Output ONLY cover letter.
"""


# ------------------------
# OLLAMA
# ------------------------

def call_ollama(
    prompt,
    model="llama3"
):

    response = requests.post(
        "http://host.docker.internal:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]


# ------------------------
# ATS RESUME
# ------------------------

def generate_ats_resume(
    profile,
    job_text
):

    raw = call_ollama(
        build_ats_prompt(
            profile,
            job_text
        )
    )

    try:

        return json.loads(raw)

    except Exception:

        return {
            "summary": raw,
            "skills": [],
            "experience": [],
            "projects": [],
            "education": []
        }


# ------------------------
# COVER LETTER
# ------------------------

def generate_cover_letter(
    profile,
    job_text
):

    return call_ollama(
        build_cover_letter_prompt(
            profile,
            job_text
        )
    )