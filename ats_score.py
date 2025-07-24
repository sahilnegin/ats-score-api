import spacy
import string
from spacy.lang.en.stop_words import STOP_WORDS

nlp = spacy.load("en_core_web_md")
stop_words = STOP_WORDS
BAD_KEYWORDS = {"look", "looking", "dev", "need", "hiring", "join", "role", "position"}
STOP_KEYWORDS = {
    "team", "candidate", "bonus", "include", "familiarity", "plus",
    "responsibility", "knowledge", "mindset", "passion", "communication",
    "platform", "point", "browser", "product"
}

def clean_and_tokenize(text: str):
    doc = nlp(text.lower())
    tokens = [
        token.lemma_ for token in doc
        if token.text not in stop_words and token.text not in string.punctuation
    ]
    return list(set(tokens))

def extract_keywords(text: str):
    doc = nlp(text.lower())
    keywords = set()
    for token in doc:
        if token.pos_ in ["NOUN", "PROPN", "VERB"] and token.text not in stop_words:
            lemma = token.lemma_
            if lemma not in BAD_KEYWORDS and lemma not in STOP_KEYWORDS:
                keywords.add(lemma)
    return list(keywords)

def calculate_ats_score(resume_text: str, job_description: str):
    resume_tokens = clean_and_tokenize(resume_text)
    jd_keywords = extract_keywords(job_description)

    matched = [kw for kw in jd_keywords if kw in resume_tokens]
    missing = [kw for kw in jd_keywords if kw not in resume_tokens]

    keyword_match_score = len(matched) / len(jd_keywords) if jd_keywords else 0
    keyword_weighted = keyword_match_score * 80

    resume_doc = nlp(resume_text)
    jd_doc = nlp(job_description)
    semantic_score = resume_doc.similarity(jd_doc) * 20

    final_score = round(keyword_weighted + semantic_score, 2)

    return {
        "ats_score": final_score,
        "matched_keywords": matched,
        "missing_keywords": missing
    }
