import chromadb

def get_collection():
    client = chromadb.PersistentClient(path="chroma_db")
    return client.get_or_create_collection(name="clothes")