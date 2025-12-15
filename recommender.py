import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_excel("Gen_AI Dataset.xlsx")

model = SentenceTransformer("all-MiniLM-L6-v2")

dataset_embeddings = model.encode(df["Query"].tolist())

def recommend(query, top_k=5):

    query_embedding = model.encode([query])

    similarities = cosine_similarity(query_embedding, dataset_embeddings)[0]

    top_indices = similarities.argsort()[-top_k:][::-1]

    results = df.iloc[top_indices]
    return results

if __name__ == "__main__":
    test_query = "I want to hire a Java developer with teamwork skills"
    results = recommend(test_query)

    print("Recommendations:")
    print(results)
