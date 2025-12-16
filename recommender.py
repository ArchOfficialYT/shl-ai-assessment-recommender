import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import re

df = pd.read_excel("Gen_AI Dataset.xlsx")

model = SentenceTransformer("all-MiniLM-L6-v2")

dataset_embeddings = model.encode(df["Query"].tolist())

def extract_assessment_name(url: str) -> str:
    """
    Convert SHL URL into a readable assessment name
    """
    slug = url.rstrip("/").split("/")[-1]
    name = slug.replace("-", " ").title()
    name = re.sub(r"\b(New|View)\b", "", name).strip()
    return name

def recommend(query, top_k=5):
    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, dataset_embeddings)[0]
    top_indices = similarities.argsort()[-top_k:][::-1]

    results = df.iloc[top_indices].copy()

    results["Assessment Name"] = results["Assessment_url"].apply(extract_assessment_name)

    return results[["Assessment Name", "Assessment_url"]]
