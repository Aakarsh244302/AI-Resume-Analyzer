import re

skills = [
    "C++", "Java", "Python", "SQL", "HTML",
    "CSS", "DSA", "DBMS", "Communication"
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

    matched = [
        skill for skill in required_skills
        if skill in resume_skills
    ]

    missing = [
        skill for skill in required_skills
        if skill not in resume_skills
    ]

    if required_skills:
        score = (len(matched) / len(required_skills)) * 100
    else:
        score = 0

    return resume_skills, matched, missing, round(score, 2)


def analyze_ats_resume(resume_text):
    score = 0
    suggestions = []

    if re.search(r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}', resume_text):
        score += 15
    else:
        suggestions.append("Add a valid email address.")

    if re.search(r'(?:\+91[\s-]?)?[6-9]\d{9}\b', resume_text):
        score += 15
    else:
        suggestions.append("Add your 10-digit mobile number.")

    sections = {
        "Education": r'\beducation\b|\bacademic background\b',
        "Skills": r'\bskills\b|\btechnical skills\b',
        "Projects": r'\bprojects\b|\bproject experience\b',
        "Experience": r'\bexperience\b|\binternship\b',
        "Certifications": r'\bcertifications\b|\bcertificates\b'
    }

    for section, pattern in sections.items():
        if re.search(pattern, resume_text, re.IGNORECASE):
            score += 8
        else:
            suggestions.append(f"Add a clear {section} section.")

    word_count = len(resume_text.split())

    if 150 <= word_count <= 1200:
        score += 15
    else:
        suggestions.append(
            "Keep resume content clear and concise (150-1200 words)."
        )

    action_words = [
        "developed", "created", "designed", "managed",
        "implemented", "improved", "built", "achieved"
    ]

    has_action_word = any(
        re.search(r'\b' + word + r'\b', resume_text, re.IGNORECASE)
        for word in action_words
    )

    has_numbers = bool(re.search(r'\b\d+%?\b', resume_text))

    if has_action_word or has_numbers:
        score += 15
    else:
        suggestions.append(
            "Add action words and measurable achievements."
        )

    return score, suggestions
