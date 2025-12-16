# SHL AI Assessment Recommender

A semantic-search based web application that recommends relevant SHL assessments
based on a natural language job requirement.

The system allows recruiters or hiring managers to input a job description and
receive the most suitable SHL assessments with direct links to the official
product pages.

---

## 🚀 Live Demo
👉 https://huggingface.co/spaces/ArchOfficialYT/shl-ai-assessment-recommender

## 📸 App Demo

![SHL AI Assessment Recommender Demo](Assessment_Recommender_Screenshot.png)

---

## 📌 Features
- Accepts free-text job descriptions
- Uses semantic similarity instead of keyword matching
- Recommends top relevant SHL assessments
- Displays clean, human-readable assessment names
- Provides clickable links to official SHL product pages
- Fully deployed and publicly accessible

---

## 🧠 Approach
1. Job descriptions are converted into vector embeddings using  
   **SentenceTransformer (`all-MiniLM-L6-v2`)**
2. Predefined SHL-related queries from the dataset are embedded offline
3. Cosine similarity is used to compare user input with dataset embeddings
4. Top-K most relevant assessments are selected
5. Assessment names are derived from SHL product URLs for clarity

---

## 🛠️ Tech Stack
- Python
- Streamlit
- Sentence Transformers
- Scikit-learn
- Pandas
- Hugging Face Spaces
