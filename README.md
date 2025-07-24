# 🧠 ATS Score API

**ATS Score API** is a fast, lightweight REST API built with FastAPI and spaCy. It simulates how real-world Applicant Tracking Systems (ATS) evaluate resumes against job descriptions — combining keyword relevance and semantic similarity to deliver a smart, realistic score.

---

### 🚀 Features

- ✅ Accepts raw text or PDF resumes
- 🧠 Combines keyword match + semantic NLP scoring
- 🛡️ Rate-limited endpoints (via SlowAPI)
- 🔌 Easily integrable into job platforms or HR tools
- ⚙️ Built with FastAPI, spaCy, and PyMuPDF

---

### 📦 Use Cases

- Resume screening and job matching
- Career platforms and resume analyzers
- HR automation and talent filters
- Developer portfolio projects (with a purpose!)

---

### 📬 API Endpoints

#### `POST /getats`
- Accepts JSON with:
  - `resume_text`: Resume content as string
  - `job_description`: Job post content
- Returns ATS score and keyword match breakdown

#### `POST /upload`
- Accepts:
  - `file`: PDF resume (via form-data)
  - `job_description`: Text field
- Returns:
  - `ats_score`: Overall match score
  - `matched_keywords`: Keywords found in resume
  - `missing_keywords`: Important terms not found

---

### 🛠️ Installation & Running

```bash
# Clone the repo
git clone https://github.com/yourusername/ats-score-api.git
cd ats-score-api

# Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Download the spaCy model
python -m spacy download en_core_web_md

# Run the API
uvicorn main:app --reload



       📤 POST /getats
            │
    ┌───────▼────────┐
    │ Save temp file │
    └───────┬────────┘
            │
    ┌───────▼────────┐
    │ parse_resume() │ ← PDF → text
    └───────┬────────┘
            │
    ┌───────▼────────────────┐
    │ calculate_ats_score()  │ ← logic & matching
    └────────┬───────────────┘
             │
    ┌────────▼───────────┐
    │ return JSON result │ → ATS Score + Matches
    └────────────────────┘
