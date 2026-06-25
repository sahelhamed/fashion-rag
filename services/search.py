from db.chroma_client import (
    get_collection
)

from services.embedder import (
    text_to_vector
)

collection = get_collection()


def search_by_text(
    text,
    n_results=3
):

    query_embedding = text_to_vector(
        text
    )

    results = collection.query(
        query_embeddings=[
            query_embedding
        ],
        n_results=n_results
    )

    return results