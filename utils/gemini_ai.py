# utils/gemini_ai.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Fetch API key from environment
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please check .env file.")

# Configure Gemini
genai.configure(api_key=api_key)

def generate_cover_letter(resume_text, jd_text):
    prompt = f"""
    Write a personalized, human-sounding cover letter for this job posting, using the candidate's resume.

    Resume:
    {resume_text}

    Job Description:
    {jd_text}

    Make it concise, enthusiastic, and natural.
    """

    try:
        model = genai.GenerativeModel("gemini-1.5-flash-latest")  # lighter model
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"❌ Gemini API Error: {e}")
        return "❌ Sorry, Gemini couldn't generate the cover letter."
