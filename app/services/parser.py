import fitz
from app.services.llm_helper import ask_local_llm

def extract_text_from_pdf(path):
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_education(text):
    prompt = f"""
    Extract education history from this resume text in JSON array format:
    [
        {{
            "degree": "",
            "institution": "",
            "years": "",
            "cgpa_or_percentile": ""
        }}
    ]

    Resume Text:
    {text}
    """
    return ask_local_llm(prompt)

def extract_experience(text):
    prompt = f"""
    Extract professional experience from resume text in JSON array format:
    [
        {{
            "title": "",
            "company": "",
            "duration": "",
            "location": "",
            "description": []
        }}
    ]

    Resume Text:
    {text}
    """
    return ask_local_llm(prompt)

def extract_skills(text):
    prompt = f"""
    Extract technical skills from the resume as a JSON list.

    Example:
    ["Python", "React", "Firebase", "SQL"]

    Resume Text:
    {text}
    """
    return ask_local_llm(prompt)

def extract_general_info(text):
    prompt = f"""
    Extract full name, email(s), and phone number(s) from resume text in this format:
    {{
        "full_name": "",
        "emails": [],
        "phone_numbers": []
    }}

    Resume Text:
    {text}
    """
    return ask_local_llm(prompt)

def extract_links_from_pdf(path):
    doc = fitz.open(path)
    links = []
    for page in doc:
        for link in page.get_links():
            if "uri" in link:
                links.append(link["uri"])
    return links

def extract_projects(text):
    prompt = f"""
    Extract project details in this format:
    [
        {{
            "title": "",
            "duration": "",
            "tech_stack": [],
            "description": ""
        }}
    ]

    Resume Text:
    {text}
    """
    return ask_local_llm(prompt)

def extract_resume_data(filename: str):
    text = extract_text_from_pdf(filename)

    return {
        "full_name_info": extract_general_info(text),
        "education": extract_education(text),
        "experience": extract_experience(text),
        "projects": extract_projects(text),
        "skills": extract_skills(text),
        "links": extract_links_from_pdf(filename)
    }


