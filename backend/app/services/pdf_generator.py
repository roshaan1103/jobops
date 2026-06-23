from pathlib import Path

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet


OUTPUT_FOLDER = (
    Path(__file__)
    .parent.parent
    / "storage"
    / "generated_resumes"
)

OUTPUT_FOLDER.mkdir(
    parents=True,
    exist_ok=True
)


def create_resume_pdf(
    ats_resume,
    profile,
    filename="resume.pdf"
):

    pdf_path = OUTPUT_FOLDER / filename

    doc = SimpleDocTemplate(
        str(pdf_path)
    )

    styles = getSampleStyleSheet()

    content = []

    # ------------------------
    # HEADER
    # ------------------------

    content.append(
        Paragraph(
            "Roshaan Ali Khan",
            styles["Title"]
        )
    )

    content.append(
        Paragraph(
            "Karachi, Pakistan",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    # ------------------------
    # SUMMARY
    # ------------------------

    content.append(
        Paragraph(
            "Professional Summary",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            ats_resume.get(
                "summary",
                ""
            ),
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 10)
    )

    # ------------------------
    # SKILLS
    # ------------------------

    content.append(
        Paragraph(
            "Skills",
            styles["Heading2"]
        )
    )

    skills = ats_resume.get(
        "skills",
        []
    )

    content.append(
        Paragraph(
            ", ".join(skills),
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 10)
    )

    # ------------------------
    # EXPERIENCE
    # ------------------------

    content.append(
        Paragraph(
            "Experience",
            styles["Heading2"]
        )
    )

    for exp in ats_resume.get(
        "experience",
        []
    ):

        content.append(
            Paragraph(
                f"<b>{exp.get('role','')}</b>",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                exp.get(
                    "company",
                    ""
                ),
                styles["Normal"]
            )
        )

        for bullet in exp.get(
            "bullets",
            []
        ):

            content.append(
                Paragraph(
                    f"• {bullet}",
                    styles["Normal"]
                )
            )

        content.append(
            Spacer(1, 8)
        )

    # ------------------------
    # PROJECTS
    # ------------------------

    content.append(
        Paragraph(
            "Projects",
            styles["Heading2"]
        )
    )

    for project in ats_resume.get(
        "projects",
        []
    ):

        content.append(
            Paragraph(
                f"<b>{project.get('title','')}</b>",
                styles["Normal"]
            )
        )

        tech_stack = project.get(
            "tech_stack",
            []
        )

        if tech_stack:

            content.append(
                Paragraph(
                    ", ".join(
                        tech_stack
                    ),
                    styles["Italic"]
                )
            )

        for bullet in project.get(
            "bullets",
            []
        ):

            content.append(
                Paragraph(
                    f"• {bullet}",
                    styles["Normal"]
                )
            )

        content.append(
            Spacer(1, 8)
        )

    # ------------------------
    # EDUCATION
    # ------------------------

    content.append(
        Paragraph(
            "Education",
            styles["Heading2"]
        )
    )

    for edu in ats_resume.get(
        "education",
        []
    ):

        content.append(
            Paragraph(
                f"{edu.get('degree','')} - {edu.get('institution','')}",
                styles["Normal"]
            )
        )

    doc.build(content)

    return str(pdf_path)