import streamlit as st
from utils.resume_parser import extract_text_from_pdf, extract_text_from_docx
from utils.jd_parser import extract_keywords
from utils.gemini_ai import generate_cover_letter, generate_tailored_resume

st.set_page_config(page_title="AI Resume Builder", layout="wide")

# -- Custom Header Styling
st.markdown("""
    <style>
        .main-title {
            text-align: center;
            font-size: 36px;
            margin-bottom: 0.2em;
        }
        .sub-title {
            text-align: center;
            font-size: 16px;
            color: #BBBBBB;
            margin-bottom: 1.5em;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>AI Resume + Cover Letter Builder</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Choose what to generate. Upload resume and job description.</div>", unsafe_allow_html=True)

# -- Output selection
gen_option = st.radio(
    "🎯 What would you like to generate?",
    ["📄 Tailored Resume", "✉️ Cover Letter", "✅ Both"],
    horizontal=True
)

st.divider()

# -- Two-column responsive layout
left_col, right_col = st.columns([1.1, 1.2])

with left_col:
    resume = st.file_uploader("📄 Resume File (PDF/DOCX)", type=["pdf", "docx"])
    jd_text = st.text_area("💼 Job Description", height=200)

    if st.button("🚀 Generate", use_container_width=True):
        if not resume or not jd_text:
            st.warning("⚠️ Please provide both resume and job description.")
        else:
            with st.spinner("Generating..."):
                resume_text = extract_text_from_pdf(resume) if resume.name.endswith(".pdf") else extract_text_from_docx(resume)
                tailored_resume = generate_tailored_resume(resume_text, jd_text) if gen_option != "✉️ Cover Letter" else None
                cover_letter = generate_cover_letter(resume_text, jd_text) if gen_option != "📄 Tailored Resume" else None

            st.session_state["resume_out"] = tailored_resume
            st.session_state["cover_out"] = cover_letter

with right_col:
    if "cover_out" in st.session_state and st.session_state["cover_out"]:
        st.subheader("✉️ Cover Letter")
        st.text_area("Cover Letter", st.session_state["cover_out"], height=250)
        st.download_button("⬇️ Download Cover Letter", st.session_state["cover_out"], file_name="cover_letter.txt", use_container_width=True)

    if "resume_out" in st.session_state and st.session_state["resume_out"]:
        st.subheader("📝 Tailored Resume")
        st.text_area("Tailored Resume", st.session_state["resume_out"], height=300)
        st.download_button("⬇️ Download Resume", st.session_state["resume_out"], file_name="tailored_resume.txt", use_container_width=True)
