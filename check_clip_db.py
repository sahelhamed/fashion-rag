import chromadb

client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_collection(
    "fashion_clip"
)

data = collection.get()

print(
    "Items:",
    len(data["ids"])
)

print(
    data["ids"]
)