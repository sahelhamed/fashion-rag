from sentence_transformers import SentenceTransformer
import chromadb

# مدل Embedding
model = SentenceTransformer("all-MiniLM-L6-v2")

# اتصال به Chroma
client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_collection("clothes")

# لباس انتخابی کاربر
selected_item = "black skirt"

query_embedding = model.encode(selected_item).tolist()

# جستجوی تاپ
tops = collection.query(
    query_embeddings=[query_embedding],
    where={"category": "top"},
    n_results=1
)

# جستجوی شرت
shirts = collection.query(
    query_embeddings=[query_embedding],
    where={"category": "shirt"},
    n_results=1
)

# جستجوی کفش
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