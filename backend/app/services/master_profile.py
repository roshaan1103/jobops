def get_devops_profile():
    return {
        "role": "DevOps Engineer",
        "skills": {
            "cloud": ["AWS", "Azure", "GCP"],
            "automation": ["CI/CD", "GitHub Actions", "GitLab CI", "Jenkins"],
            "security": ["IAM", "DevSecOps", "Trivy", "CodeQL", "RBAC"],
            "monitoring": ["Prometheus", "Grafana", "CloudWatch", "ELK"],
            "programming": ["Python", "Bash", "Go"],
            "other": ["Linux", "Docker", "Kubernetes", "Terraform", "Ansible"]
        },
        "projects": [
            {
                "title": "Self-Healing AI-Driven Kubernetes Platform ",
                "tech_stack": ["Kubernetes", "ArgoCD", "Prometheus", "Grafana", "FastAPI"],
                "bullets": [
                    "Built an AIOps platform capable of detecting infrastructure anomalies and triggering automated remediation in Kubernetes clusters",
                    "Implemented GitOps workflows using ArgoCD for automated deployments and Kubernetes configuration synchronization",
                    "Developed ML-based anomaly detection services using Isolation Forest models for real-time telemetry analysis",
                    "Integrated Prometheus, Alertmanager, and Grafana for monitoring, alerting, and infrastructure observability",
                    "Automated CI/CD pipelines using GitHub Actions to build, deploy, and update Kubernetes workloads dynamically"
                ]
            },
            {
                "title": "Cloud-Native DevSecOps CI/CD Pipeline",
                "tech_stack": ["AWS", "Docker", "GitHub Actions", "CloudWatch"],
                "bullets": [
                    "Designed and deployed a secure CI/CD pipeline for containerized applications on AWS EC2 with automated deployments",
                    "Integrated CodeQL and Trivy scanning to enforce shift-left security and container vulnerability detection",
                    "Implemented hardened Docker runtime configurations using non-root containers and read-only filesystems",
                    "Built centralized observability pipelines using CloudWatch dashboards, alarms, and structured application logging"
                ]
            }
        ],
        "experience": [
            {
                "company": "DevOps Internship",
                "role": "DevOps & AI Ops Intern",
                "date": "May 2024– May 2025",
                "location": "Karachi, Pakistan",
                "bullets": [
                    "Built and managed containerized environments using Docker and Podman across Linux-based systems and Kubernetes workloads",
                    "Developed Python automation scripts and CLI utilities to streamline infrastructure and operational tasks",
                    "Worked with Kubernetes deployments, troubleshooting, networking, and monitoring in simulated production-style environments",
                    "Implemented monitoring and logging workflows to improve infrastructure observability and incident debugging",
                    "Applied networking and security concepts including firewall configuration, secure file transfer, and intrusion detection systems"
                ]
            }
        ],
        "education": [
            {
                "institution": "Al-Nafi International College",
                "degree": "EduQual Level 6 in Artificial Intelligence Operations (AiOps)",
                "date": "May 2024– May 2026",
                "location": "Karachi, Pakistan",
            },
            {
                "institution": "Beacon Light Academy",
                "degree": "Edexcel A-Levels in Information Technology",
                "date": "Aug 2020– Jun 2022",
                "location": "Karachi, Pakistan",
            }
        ]
    }


def get_cloud_profile():
    return {
        "role": "Cloud Engineer",
        "skills": {
            "cloud": ["AWS", "Azure", "GCP", "IAM", "CloudWatch"],
            "automation": ["Terraform", "CI/CD", "GitHub Actions"],
            "security": ["Cloud Security", "IAM Policies", "KMS"],
            "monitoring": ["CloudWatch", "Grafana", "Prometheus"],
            "programming": ["Python", "Bash"],
            "other": ["Linux", "Networking"]
        },
        "projects": [
            {
                "title": "AI-Powered Cloud Security & IAM Analyzer ",
                "tech_stack": ["AWS", "Terraform", "Python","Cloud Security"],
                "bullets": [
                    "Built a cloud security analysis platform to detect IAM and S3 misconfigurations across AWS environments",
                    "Developed IAM risk detection workflows identifying wildcard access, privilege escalation paths, and over-permissive policies",
                    "Implemented CloudTrail-driven least privilege analysis to derive minimal IAM permissions from API usage logs",
                    "Integrated automated Terraform remediation generation for secure infrastructure corrections",
                    "Implemented IAM policy validation and access simulation using AWS APIs before deployment"
                ]
            },
            {
                "title": "AI-Powered Threat Detection & Log Intelligence System",
                "tech_stack": ["Python", "FastAPI", "Docker", "Scikit-learn"],
                "bullets": [
                    "Developed an AI-driven security log analysis platform to detect brute-force and credential stuffing attacks",
                    "Implemented hybrid anomaly detection using Isolation Forest and rule-based detection logic",
                    "Integrated MITRE ATT&CK mapping for standardized threat classification and security event analysis",
                    "Containerized the platform using Docker for scalable deployment across environments"


                ]
             }
        ],
        "experience": [],
        "education": []
    }


def get_master_profile():
    """
    Merge both profiles into one ATS source of truth
    """
    devops = get_devops_profile()
    cloud = get_cloud_profile()

    def merge_lists(a, b):
        return list({*a, *b})

    merged = {
        "skills": {
            k: merge_lists(devops["skills"].get(k, []),
                          cloud["skills"].get(k, []))
            for k in devops["skills"]
        },
        "projects": devops["projects"] + cloud["projects"],
        "experience": devops["experience"],
        "education": devops["education"]
    }

    return merged