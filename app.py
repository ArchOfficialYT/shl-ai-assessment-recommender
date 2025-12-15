from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

df = pd.read_excel("Gen_AI Dataset.xlsx")
model = SentenceTransformer("all-MiniLM-L6-v2")
dataset_embeddings = model.encode(df["Query"].tolist())

class RecommendRequest(BaseModel):
    query: str

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/recommend")
def recommend_assessments(request: RecommendRequest):
    query_embedding = model.encode([request.query])
    similarities = cosine_similarity(query_embedding, dataset_embeddings)[0]
    top_indices = similarities.argsort()[-5:][::-1]

    results = []
    for idx in top_indices:
        results.append({
            "assessment_name": df.iloc[idx]["Query"],
            "url": df.iloc[idx]["Assessment_url"]
        })

    return {"recommended_assessments": results}
