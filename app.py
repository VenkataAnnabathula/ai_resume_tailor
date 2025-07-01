# app.py
import streamlit as st
from utils.resume_parser import extract_text_from_pdf, extract_text_from_docx
from utils.jd_parser import extract_keywords
from utils.gemini_ai import generate_cover_letter  # ✅ Moved to the top

st.set_page_config(page_title="AI Resume Tailor", layout="centered")

st.title("🧠 AI Resume + Cover Letter Tailor")
st.markdown("Upload your resume and job description. Get customized documents instantly.")

resume = st.file_uploader("📄 Upload your resume (PDF or DOCX)", type=["pdf", "docx"])
jd_text = st.text_area("💼 Paste the job description here", height=300)

if st.button("🚀 Generate Resume & Cover Letter"):
    if not resume or not jd_text:
        st.warning("Please upload both your resume and job description.")
    else:
        # Extract resume text
        if resume.name.endswith(".pdf"):
            resume_text = extract_text_from_pdf(resume)
        else:
            resume_text = extract_text_from_docx(resume)

        # Extract keywords from JD
        jd_keywords = extract_keywords(jd_text)

        st.subheader("📄 Extracted Resume Text")
        st.code(resume_text[:1000] + "...", language='text')

        st.subheader("🔍 Job Description Keywords")
        st.write(jd_keywords[:20])  # preview top 20

        # ✅ Generate Cover Letter using Gemini
        cover_letter = generate_cover_letter(resume_text, jd_text)

        st.subheader("✉️ Generated Cover Letter")
        st.text_area("Result", value=cover_letter, height=300)
