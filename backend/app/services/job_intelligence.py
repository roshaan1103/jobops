import re
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")


# -----------------------------
# 1. BASIC CLEANING
# -----------------------------
def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    return text.strip().lower()


# -----------------------------
# 2. AI SKILL EXTRACTION (soft NLP)
# -----------------------------
COMMON_SKILLS = [

    # Programming
    "python",
    "java",
    "go",
    "bash",
    "shell",

    # OS
    "linux",
    "ubuntu",
    "centos",

    # Containers
    "docker",
    "kubernetes",
    "helm",

    # CI/CD
    "jenkins",
    "github actions",
    "gitlab ci",
    "ci/cd",

    # Cloud
    "aws",
    "azure",
    "gcp",

    # IaC
    "terraform",
    "ansible",
    "cloudformation",

    # Monitoring
    "prometheus",
    "grafana",
    "elk",
    "elasticsearch",
    "logstash",
    "kibana",

    # Backend
    "fastapi",
    "flask",
    "django",
    "node.js",

    # Database
    "postgresql",
    "mysql",
    "mongodb",
    "redis",
    "sql",

    # Networking
    "dns",
    "tcp/ip",
    "http",
    "https",
    "load balancing",

    # Security
    "devsecops",
    "security",
    "iam",

    # AI / AIOps
    "machine learning",
    "deep learning",
    "nlp",
    "pytorch",
    "tensorflow",
    "aiops",

]

def extract_skills(text: str):

    text = text.lower()

    found = []

    for skill in COMMON_SKILLS:

        if skill.lower() in text:
            found.append(skill)

    return sorted(list(set(found)))


# -----------------------------
# 3. SENIORITY DETECTION
# -----------------------------
def detect_seniority(text: str) -> str:
    text = text.lower()

    if "senior" in text or "lead" in text or "architect" in text:
        return "senior"

    if "junior" in text or "intern" in text or "entry" in text or "associate" in text:
        return "junior"

    return "mid"


# -----------------------------
# 4. ROLE DETECTION
# -----------------------------
def detect_role(text: str):

    text = text.lower()

    role_map = {

        "devops engineer": [
            "devops",
            "site reliability engineer",
            "sre",
            "platform engineer",
            "infrastructure engineer",
            "release engineer",
            "build engineer"
        ],

        "cloud engineer": [
            "cloud engineer",
            "cloud administrator",
            "cloud specialist",
            "aws engineer",
            "azure engineer",
            "gcp engineer"
        ],

        "cloud architect": [
            "cloud architect",
            "solutions architect"
        ],

        "devsecops engineer": [
            "devsecops",
            "security engineer",
            "cloud security engineer"
        ],

        "backend engineer": [
            "backend",
            "software engineer",
            "python developer"
        ],

        "data engineer": [
            "data engineer",
            "data platform engineer"
        ],

        "ml engineer": [
            "machine learning engineer",
            "ml engineer",
            "ai engineer"
        ]
    }

    for role, keywords in role_map.items():

        for keyword in keywords:

            if keyword in text:
                return role

    return "unknown"

# -----------------------------
# 5. EXPERIENCE, EDUCATION AND CERTIFICATION
# -----------------------------

def extract_experience(text: str):

    patterns = [

        r'(\d+)\+?\s*years',

        r'(\d+)\s*-\s*(\d+)\s*years',

        r'minimum\s*(\d+)\s*years'
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            text.lower()
        )

        if match:
            return match.group(0)

    return None

def extract_education(text: str):

    text = text.lower()

    education = []

    keywords = [

        "bachelor",

        "bachelors",

        "bs",

        "bsc",

        "master",

        "masters",

        "ms",

        "msc",

        "phd"
    ]

    for keyword in keywords:

        if keyword in text:
            education.append(keyword)

    return list(set(education))

def extract_certifications(text: str):

    text = text.lower()

    certs = []

    known = [

        "aws certified",

        "solutions architect",

        "developer associate",

        "sysops administrator",

        "azure administrator",

        "azure fundamentals",

        "azure architect",

        "cka",

        "ckad",

        "cks",

        "terraform associate",

        "comptia security+",

        "cissp"
    ]

    for cert in known:

        if cert in text:
            certs.append(cert)

    return certs

# -----------------------------
# 5. EMBEDDING (for matching)
# -----------------------------
def get_embedding(text: str):
    return model.encode(text)


# -----------------------------
# 6. FULL JOB INTELLIGENCE PIPELINE
# -----------------------------
def analyze_job(text: str):

    cleaned = clean_text(text)

    return {

        "clean_text": cleaned,

        "skills": extract_skills(cleaned),

        "role": detect_role(cleaned),

        #"domain": detect_domain(cleaned),

        "experience": extract_experience(cleaned),

        "education": extract_education(cleaned),

        "certifications": extract_certifications(cleaned),

        "seniority": detect_seniority(cleaned),

        "embedding": get_embedding(cleaned)
    }