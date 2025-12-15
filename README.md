# SHL AI Assessment Recommendation System

This project implements a semantic recommendation system to suggest relevant SHL assessments based on natural language job requirements.

## Approach
- Sentence embeddings are generated using `all-MiniLM-L6-v2`
- Cosine similarity is used to find the most relevant assessments
- A FastAPI backend exposes recommendation endpoints

## API Endpoints
- `GET /health` – Health check
- `POST /recommend` – Returns top assessment recommendations

## How to run locally
```bash
pip install -r requirements.txt
python -m uvicorn app:app
