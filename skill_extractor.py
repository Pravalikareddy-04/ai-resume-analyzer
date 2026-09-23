import pandas as pd
import os
import re


def load_skill_dictionary(
    file_path="data/skill_dictionary.csv"
):

    if not os.path.exists(file_path):

        return []

    try:

        df = pd.read_csv(file_path)

        if "Skill" not in df.columns:

            return []

        return (
            df["Skill"]
            .dropna()
            .astype(str)
            .tolist()
        )

    except Exception:

        return []


def extract_skills(
    text,
    dictionary_path="data/skill_dictionary.csv"
):

    if not text:

        return []

    text = text.lower()

    skills = load_skill_dictionary(dictionary_path)

    detected_skills = []

    for skill in skills:

        skill_clean = skill.strip()

        if not skill_clean:
            continue

        pattern = r"(?<!\w)" + re.escape(
            skill_clean.lower()
        ) + r"(?!\w)"

        if re.search(pattern, text):

            detected_skills.append(skill_clean)

    # Remove duplicates
    detected_skills = list(
        dict.fromkeys(detected_skills)
    )

    return detected_skills