import chromadb

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_collection("clothes")

print(
    collection.get(
        include=["documents", "metadatas"]
    )
)