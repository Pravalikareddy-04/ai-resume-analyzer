import streamlit as st
import os
import pandas as pd

from resume_parser import extract_resume_text
from text_cleaner import clean_text
from skill_extractor import extract_skills
from job_matcher import match_jobs
from roadmap_generator import generate_roadmap


st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


st.title("📄 AI Resume Analyzer & Job Recommendation System")
st.write(
    "Upload your resume to extract skills, analyze your profile, "
    "get suitable job recommendations, and view a learning roadmap."
)


# ---------------------------------------------------------
# File Upload
# ---------------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload your resume",
    type=["pdf", "docx", "txt"]
)


if uploaded_file is not None:

    os.makedirs("sample_resumes", exist_ok=True)

    file_path = os.path.join(
        "sample_resumes",
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Resume uploaded successfully! ✅")

    # -----------------------------------------------------
    # Extract Resume Text
    # -----------------------------------------------------

    with st.spinner("Reading resume..."):

        resume_text = extract_resume_text(file_path)

    if not resume_text.strip():

        st.error(
            "Could not extract text from the resume. "
            "Please upload a text-based PDF, DOCX, or TXT file."
        )

    else:

        # -------------------------------------------------
        # Clean Text
        # -------------------------------------------------

        cleaned_text = clean_text(resume_text)

        # -------------------------------------------------
        # Extract Skills
        # -------------------------------------------------

        skills = extract_skills(cleaned_text)

        # -------------------------------------------------
        # Resume Preview
        # -------------------------------------------------

        with st.expander("📃 Resume Text Preview"):

            st.write(resume_text[:5000])

        # -------------------------------------------------
        # Skills
        # -------------------------------------------------

        st.subheader("🛠️ Skills Detected")

        if skills:

            skill_columns = st.columns(4)

            for i, skill in enumerate(skills):

                skill_columns[i % 4].success(skill)

        else:

            st.warning(
                "No matching skills were detected in the resume."
            )

        # -------------------------------------------------
        # Job Matching
        # -------------------------------------------------

        st.subheader("💼 Recommended Job Roles")

        jobs = match_jobs(
            cleaned_text,
            skills,
            "data/job_roles.csv"
        )

        if not jobs.empty:

            display_columns = [
                "Job Role",
                "Matched Skills",
                "Match Percentage",
                "Missing Skills"
            ]

            st.dataframe(
                jobs[display_columns],
                use_container_width=True,
                hide_index=True
            )

            # -------------------------------------------------
            # Detailed Job Recommendations
            # -------------------------------------------------

            st.subheader("📊 Job Match Details")

            for _, row in jobs.iterrows():

                with st.expander(
                    f"{row['Job Role']} — {row['Match Percentage']}%"
                ):

                    st.write(
                        f"**Matched Skills:** "
                        f"{row['Matched Skills']}"
                    )

                    st.write(
                        f"**Missing Skills:** "
                        f"{row['Missing Skills']}"
                    )

        else:

            st.warning("No job roles found.")

        # -------------------------------------------------
        # Learning Roadmap
        # -------------------------------------------------

        st.subheader("🗺️ Personalized Learning Roadmap")

        roadmap = generate_roadmap(
            skills,
            jobs
        )

        if roadmap:

            for item in roadmap:

                st.write(
                    f"**{item['Priority']}. {item['Skill']}**"
                )

                st.write(
                    f"Reason: {item['Reason']}"
                )

        else:

            st.info(
                "Your detected skills match the available "
                "job roles well. Keep improving your existing skills!"
            )

        # -------------------------------------------------
        # Download Report
        # -------------------------------------------------

        report_text = "AI RESUME ANALYZER REPORT\n"
        report_text += "=" * 50 + "\n\n"

        report_text += "DETECTED SKILLS\n"
        report_text += "-" * 30 + "\n"

        for skill in skills:

            report_text += f"- {skill}\n"

        report_text += "\nRECOMMENDED JOB ROLES\n"
        report_text += "-" * 30 + "\n"

        if not jobs.empty:

            for _, row in jobs.iterrows():

                report_text += (
                    f"\nJob Role: {row['Job Role']}\n"
                    f"Match: {row['Match Percentage']}%\n"
                    f"Matched Skills: {row['Matched Skills']}\n"
                    f"Missing Skills: {row['Missing Skills']}\n"
                )

        report_text += "\nLEARNING ROADMAP\n"
        report_text += "-" * 30 + "\n"

        for item in roadmap:

            report_text += (
                f"\n{item['Priority']}. "
                f"{item['Skill']}\n"
                f"Reason: {item['Reason']}\n"
            )

        st.download_button(
            label="📥 Download Analysis Report",
            data=report_text,
            file_name="resume_analysis_report.txt",
            mime="text/plain"
        )