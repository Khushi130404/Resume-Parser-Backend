import fitz
from app.services.llm_helper import ask_local_llm

def extract_text_from_pdf(path):
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_links_from_pdf(path):
    doc = fitz.open(path)
    links = []
    for page in doc:
        for link in page.get_links():
            if "uri" in link:
                links.append(link["uri"])
    return links

def extract_resume_data(filename: str):
    text = extract_text_from_pdf(filename)
    links = extract_links_from_pdf(filename)

    prompt = f"""
    You are a professional resume parser. From the following resume text, extract structured information in JSON format.

    Use the following format:
    {{
    "full_name": "",
    "emails": [],
    "phone_numbers": [],
    "education": [
        {{
        "degree": "",
        "institution": "",
        "years": "",
        "cgpa_or_percentile": ""
        }}
    ],
    "experience": [
        {{
        "title": "",
        "company": "",
        "duration": "",
        "location": "",
        "description": []
        }}
    ],
    "projects": [
        {{
        "title": "",
        "duration": "",
        "tech_stack": [],
        "description": ""
        }}
    ],
    "skills": [],
    "links": {{
        "linkedin": "",
        "github": "",
        "leetcode": ""
    }}
    }}

    Resume Text:
    {text}
    """

    structured_info = ask_local_llm(prompt)

    return {
        "text_summary": structured_info,
        "extracted_links": links
    }
