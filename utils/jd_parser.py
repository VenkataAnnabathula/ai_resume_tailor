# utils/jd_parser.py
import re

def extract_keywords(text):
    # Simple keyword extraction — later we’ll use NLP
    keywords = re.findall(r'\b[A-Za-z]{4,}\b', text.lower())
    return list(set(keywords))

