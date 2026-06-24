import chromadb
from config import DB_PATH, COLLECTION_NAME

def get_collection():
    client = chromadb.PersistentClient(path=DB_PATH)
    return client.get_or_create_collection(name=COLLECTION_NAME)