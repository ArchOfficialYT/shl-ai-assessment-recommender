import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_excel("Gen_AI Dataset.xlsx")

model = SentenceTransformer("all-MiniLM-L6-v2")
dataset_embeddings = model.encode(df["Query"].tolist())

def recommend_urls(query, top_k=5):
    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, dataset_embeddings)[0]
    top_indices = similarities.argsort()[-top_k:][::-1]

    urls = []
    for idx in top_indices:
        urls.append(df.iloc[idx]["Assessment_url"])
    return urls


test_queries = df["Query"].unique()

rows = []

for query in test_queries:
    urls = recommend_urls(query)
    for url in urls:
        rows.append({
            "Query": query,
            "Assessment_url": url
        })


output_df = pd.DataFrame(rows)
output_df.to_csv("submission_predictions.csv", index=False)

print("submission_predictions.csv generated successfully!")
