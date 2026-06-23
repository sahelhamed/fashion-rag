from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_collection("clothes")

selected_item = input("Select item: ")

query_embedding = model.encode(selected_item).tolist()

# اول خود آیتم را پیدا کن
result = collection.query(
    query_embeddings=[query_embedding],
    n_results=1
)

category = result["metadatas"][0][0]["category"]

print("\nDetected category:", category)

print("\nStyle Suggestion\n")

print("Selected:")
print("-", selected_item)

# قوانین استایل
if category == "skirt":

    tops = collection.query(
        query_embeddings=[query_embedding],
        where={"category": "top"},
        n_results=2
    )

    print("\nTop:")
    for item in tops["documents"][0]:
        print("-", item)

    shoes = collection.query(
        query_embeddings=[query_embedding],
        where={"category": "shoes"},
        n_results=2
    )

    print("\nShoes:")
    for item in shoes["documents"][0]:
        print("-", item)


elif category in ["top", "shirt"]:

    bottoms = collection.query(
        query_embeddings=[query_embedding],
        where={"category": "skirt"},
        n_results=2
    )

    print("\nBottoms:")
    for item in bottoms["documents"][0]:
        print("-", item)

    shoes = collection.query(
        query_embeddings=[query_embedding],
        where={"category": "shoes"},
        n_results=2
    )

    print("\nShoes:")
    for item in shoes["documents"][0]:
        print("-", item)


elif category == "shoes":

    tops = collection.query(
        query_embeddings=[query_embedding],
        where={"category": "top"},
        n_results=2
    )

    shirts = collection.query(
        query_embeddings=[query_embedding],
        where={"category": "shirt"},
        n_results=2
    )

    print("\nTops:")
    for item in tops["documents"][0]:
        print("-", item)

    print("\nShirts:")
    for item in shirts["documents"][0]:
        print("-", item)