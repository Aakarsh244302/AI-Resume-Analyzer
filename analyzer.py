
import re

skills = [
    "C++",
    "Java",
    "Python",
    "SQL",
    "HTML",
    "CSS",
    "DSA",
    "DBMS",
    "Communication"
]

def find_skills(text):

    found_skills = []

    for skill in skills:

        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        if re.search(pattern, text, re.IGNORECASE):
            found_skills.append(skill)

    return found_skills


def analyze_resume(resume_text, job_description):

    resume_skills = find_skills(resume_text)
    required_skills = find_skills(job_description)

    matched = []

    for skill in required_skills:
        if skill in resume_skills:
            matched.append(skill)

    if len(required_skills) > 0:
        score = (len(matched) / len(required_skills)) * 100
    else:
        score = 0

    missing = []

    for skill in required_skills:
        if skill not in resume_skills:
            missing.append(skill)

    return resume_skills, matched, missing, round(score, 2)
