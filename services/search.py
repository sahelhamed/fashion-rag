from db.chroma_client import get_collection

collection = get_collection()

def search(vector, k=3):
    return collection.query(
        query_embeddings=[vector],
        n_results=k
    )