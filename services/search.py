from db.chroma_client import (
    get_collection
)

collection = get_collection()


def search_by_vector(
    vector,
    n_results=3
):
    return collection.query(
        query_embeddings=[vector],
        n_results=n_results
    )