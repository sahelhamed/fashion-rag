import os
from sentence_transformers import SentenceTransformer
from db import reset_collection

model = SentenceTransformer("all-MiniLM-L6-v2")
collection = reset_collection()

image_folder = "images"

def get_category(filename):
    name = filename.lower()
    if "shoe" in name or "sneaker" in name or "boot" in name:
        return "shoes"
    elif "skirt" in name or "pants" in name:
        return "bottom"
    elif "shirt" in name or "top" in name:
        return "top"
    else:
        return "unknown"

items = []

for file in os.listdir(image_folder):
    if file.endswith((".jpg", ".png")):
        text = file.replace("_", " ").replace(".jpg", "").replace(".png", "")

        items.append({
            "id": file,
            "text": text,
            "category": get_category(file)
        })

collection.delete()  # 🔥 پاک کردن دیتابیس قبلی (خیلی مهم)

for item in items:
    embedding = model.encode(item["text"]).tolist()

    collection.add(
        ids=[item["id"]],
        embeddings=[embedding],
        documents=[item["text"]],
        metadatas=[{"category": item["category"]}]
    )

print("DB built successfully")
print("Items:", len(items))