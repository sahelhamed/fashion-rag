import os
from sentence_transformers import SentenceTransformer
import chromadb

# مدل embedding
model = SentenceTransformer("all-MiniLM-L6-v2")

# اتصال به Chroma
client = chromadb.PersistentClient(path="chroma_db")

# اگر قبلاً ساخته شده حذفش کن
try:
    client.delete_collection("clothes")
except:
    pass

collection = client.create_collection("clothes")

image_folder = "images"

for file in os.listdir(image_folder):

    if not (file.endswith(".jpg") or file.endswith(".png")):
        continue

    text = (
        file.replace(".jpg", "")
        .replace(".png", "")
        .replace("_", " ")
    )

    # تشخیص دسته از اسم فایل
    category = "unknown"

    if "skirt" in file.lower():
        category = "skirt"

    elif "top" in file.lower():
        category = "top"

    elif "shirt" in file.lower():
        category = "shirt"

    elif "shoes" in file.lower():
        category = "shoes"

    embedding = model.encode(text).tolist()

    collection.add(
        ids=[file],
        embeddings=[embedding],
        documents=[text],
        metadatas=[
            {
                "category": category
            }
        ]
    )

print("DB built successfully")
print("Items:", collection.count())