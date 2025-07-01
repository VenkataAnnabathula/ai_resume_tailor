# utils/gemini_ai.py
import google.generativeai as genai

# Use MakerSuite key directly
genai.configure(api_key="AIzaSyAvCF503BcB3XB-kQuuqtFLXnjG88BwIEo")

def generate_cover_letter(resume_text, jd_text):
    prompt = f"""
    Write a personalized, human-sounding cover letter for this job posting, using the candidate's resume.

    Resume:
    {resume_text}

    Job Description:
    {jd_text}

    Make it concise, enthusiastic, and natural.
    """

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text
