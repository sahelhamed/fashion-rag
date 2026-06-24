from db.chroma_client import get_collection
from services.stylist import suggest_outfit

collection = get_collection()

selected = input("Select item: ")

item = collection.get(ids=[selected])

if not item["ids"]:
    print("Item not found!")
    exit()

meta = item["metadatas"][0]
category = meta.get("category", "unknown")

print("\nDetected category:", category)

print("\nSelected:")
print("-", selected)

suggest_outfit(category)