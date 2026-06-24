import os
from config import IMAGE_FOLDER
from db.chroma_client import get_collection
from services.embedder import image_to_vector

collection = get_collection()

def get_category(filename):
    name = filename.lower()

    if "shoe" in name or "boot" in name or "sneaker" in name:
        return "shoes"
    elif "skirt" in name or "pants" in name:
        return "bottom"
    elif "shirt" in name or "top" in name:
        return "top"
    else:
        return "unknown"


# reset DB (safe)
try:
    collection.delete()
except:
    pass

count = 0

for file in os.listdir(IMAGE_FOLDER):
    if not file.lower().endswith((".jpg", ".png", ".jpeg")):
        continue

    path = os.path.join(IMAGE_FOLDER, file)

    vector = image_to_vector(path)
    category = get_category(file)

    collection.add(
        ids=[file],
        embeddings=[vector],
        documents=[file],
        metadatas=[{"category": category}]
    )

    print("Added:", file)
    count += 1

print("\nDB built successfully")
print("Items:", count)