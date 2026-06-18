from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_collection("clothes")

selected_item = input("Select item: ")

query_embedding = model.encode(selected_item).tolist()

tops = collection.query(
    query_embeddings=[query_embedding],
    where={"category": "top"},
    n_results=1
)

shirts = collection.query(
    query_embeddings=[query_embedding],
    where={"category": "shirt"},
    n_results=1
)

shoes = collection.query(
    query_embeddings=[query_embedding],
    where={"category": "shoes"},
    n_results=1
)

print("\nStyle Suggestion\n")

print("Selected:")
print("-", selected_item)

print("\nTop:")

for item in tops["documents"][0]:
    print("-", item)

for item in shirts["documents"][0]:
    print("-", item)

print("\nShoes:")

for item in shoes["documents"][0]:
    print("-", item)