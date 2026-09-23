def generate_roadmap(
    resume_skills,
    jobs
):

    resume_skill_set = {
        skill.lower().strip()
        for skill in resume_skills
    }

    missing_skills = {}

    if jobs is not None and not jobs.empty:

        # Consider the top 3 recommended jobs
        top_jobs = jobs.head(3)

        for _, row in top_jobs.iterrows():

            skills = str(
                row["Missing Skills"]
            ).split(",")

            for skill in skills:

                skill = skill.strip()

                if skill and skill.lower() != "none":

                    key = skill.lower()

                    if key not in missing_skills:

                        missing_skills[key] = {
                            "Skill": skill,
                            "Count": 0,
                            "Jobs": []
                        }

                    missing_skills[key]["Count"] += 1

                    missing_skills[key]["Jobs"].append(
                        row["Job Role"]
                    )

    # Sort according to number of job roles requiring skill
    ordered = sorted(
        missing_skills.values(),
        key=lambda x: x["Count"],
        reverse=True
    )

    roadmap = []

    for index, item in enumerate(
        ordered[:10],
        start=1
    ):

        jobs_text = ", ".join(
            item["Jobs"]
        )

        roadmap.append({

            "Priority": index,

            "Skill": item["Skill"],

            "Reason": (
                f"This skill is useful for "
                f"{jobs_text}."
            )

        })

    return roadmap