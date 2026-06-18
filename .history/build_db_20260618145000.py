import os
from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer('all-MiniLM-L6-v2')

client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection(name="clothes")

image_folder = "images"

for file in os.listdir(image_folder):
    if file.endswith(".jpg") or file.endswith(".png"):

        text = file.replace("_", " ").replace(".jpg", "")

        embedding = model.encode(text).tolist()

        collection.add(
            ids=[file],
            embeddings=[embedding],
            documents=[text]
        )

print("✅ DB built once")