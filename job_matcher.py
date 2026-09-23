import pandas as pd
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_jobs(file_path):

    if not os.path.exists(file_path):

        return pd.DataFrame()

    df = pd.read_csv(file_path)

    required_columns = [
        "Job Role",
        "Skills",
        "Description"
    ]

    for column in required_columns:

        if column not in df.columns:

            raise ValueError(
                f"Missing column: {column}"
            )

    return df


def match_jobs(
    resume_text,
    resume_skills,
    file_path="data/job_roles.csv"
):

    jobs = load_jobs(file_path)

    if jobs.empty:

        return pd.DataFrame()

    resume_text = str(resume_text)

    job_descriptions = (
        jobs["Description"]
        .fillna("")
        .astype(str)
        .tolist()
    )

    documents = [
        resume_text
    ] + job_descriptions

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    try:

        matrix = vectorizer.fit_transform(
            documents
        )

        similarity_scores = cosine_similarity(
            matrix[0:1],
            matrix[1:]
        )[0]

    except ValueError:

        similarity_scores = [
            0
        ] * len(jobs)

    results = []

    resume_skill_set = {
        skill.lower().strip()
        for skill in resume_skills
    }

    for index, row in jobs.iterrows():

        job_skills = [
            skill.strip()
            for skill in str(row["Skills"]).split(",")
            if skill.strip()
        ]

        job_skill_set = {
            skill.lower()
            for skill in job_skills
        }

        matched = (
            resume_skill_set
            .intersection(job_skill_set)
        )

        missing = (
            job_skill_set
            - resume_skill_set
        )

        if job_skill_set:

            skill_percentage = (
                len(matched)
                / len(job_skill_set)
            ) * 100

        else:

            skill_percentage = 0

        tfidf_percentage = (
            similarity_scores[index] * 100
        )

        # Combine skill matching and TF-IDF
        final_score = (
            skill_percentage * 0.7
            + tfidf_percentage * 0.3
        )

        final_score = min(
            round(final_score, 2),
            100
        )

        results.append({

            "Job Role": row["Job Role"],

            "Matched Skills": (
                ", ".join(
                    sorted(matched)
                )
                if matched
                else "None"
            ),

            "Match Percentage": final_score,

            "Missing Skills": (
                ", ".join(
                    sorted(missing)
                )
                if missing
                else "None"
            )

        })

    result_df = pd.DataFrame(results)

    result_df = result_df.sort_values(
        by="Match Percentage",
        ascending=False
    )

    return result_df.reset_index(
        drop=True
    )