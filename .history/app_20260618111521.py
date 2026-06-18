import os
from sentence_transformers import SentenceTransformer
import chromadb

# 1. مدل embedding
model = SentenceTransformer('all-MiniLM-L6-v2')

# 2. ساخت دیتابیس vector
client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection(name="clothes")

# 3. خواندن عکس‌ها
image_folder = "images"

items = []

for file in os.listdir(image_folder):
    if file.endswith(".jpg") or file.endswith(".png"):
        # تبدیل اسم فایل به متن ساده
        text = file.replace("_", " ").replace(".jpg", "")

        items.append({
            "id": file,
            "text": text
        })

# 4. embedding + ذخیره
for item in items:
    embedding = model.encode(item["text"]).tolist()

    collection.add(
        ids=[item["id"]],
        embeddings=[embedding],
        documents=[item["text"]]
    )

print("✅ Database created!")