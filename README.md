# SHL AI Assessment Recommender

A semantic-search based recommendation system that suggests relevant SHL assessments
based on a natural language job requirement.

## 🚀 Live Demo
👉 https://huggingface.co/spaces/ArchOfficialYT/shl-ai-assessment-recommender

## 📌 Features
- Accepts free-text job descriptions
- Uses Sentence Transformers for semantic similarity
- Recommends top matching SHL assessments
- Clean assessment names extracted from URLs
- Clickable links to official SHL product pages
- Fully deployed & publicly accessible

## 🧠 Approach
1. Job descriptions are embedded using `all-MiniLM-L6-v2`
2. Cosine similarity is used to match against known SHL queries
3. Top-K relevant assessments are returned
4. Assessment names are derived from product URLs

## 🛠️ Tech Stack
- Python
- Streamlit
- Sentence Transformers
- Scikit-learn
- Pandas
- Hugging Face Spaces

## 📂 Project Structure
├── streamlit_app.py
├── recommender.py
├── Gen_AI Dataset.xlsx
├── requirements.txt
└── README.md

## ▶️ Run Locally
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py


📌 **Commit message:**  
`Update README with live demo and explanation`

---

### 🔹 B. Repo Checklist (quick scan)

Make sure:
- ✅ `requirements.txt` exists
- ✅ `streamlit_app.py` is root-level
- ✅ `recommender.py` is root-level
- ✅ Dataset file is committed
- ❌ No `.env` or secrets

---

## ✅ 3. SUBMISSION: WHAT LINK TO SHARE?

When submitting (Google Form / email / portal):

**Primary Link (MOST IMPORTANT):**
https://huggingface.co/spaces/ArchOfficialYT/shl-ai-assessment-recommender


**Secondary (Code):**
https://github.com/ArchOfficialYT/fynd-ai-assignment
