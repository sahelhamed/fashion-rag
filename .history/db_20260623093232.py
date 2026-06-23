import chromadb

DB_PATH = "chroma_db"
COLLECTION_NAME = "clothes"


def get_client():
    return chromadb.PersistentClient(path=DB_PATH)


def get_collection():
    client = get_client()
    return client.get_or_create_collection(
        name=COLLECTION_NAME
    )


def reset_collection():
    client = get_client()

    try:
        client.delete_collection(COLLECTION_NAME)
    except:
        pass

    return client.get_or_create_collection(
        name=COLLECTION_NAME
    )