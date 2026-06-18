from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer('all-MiniLM-L6-v2')

client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_collection(name="clothes")

query = "blue skirt"

query_embedding = model.encode(query).tolist()

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)

print("\n🎀 پیشنهاد استایل برای شما:\n")

for doc in results["documents"][0]:
    print("-", doc)