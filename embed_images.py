from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch
import chromadb
import os

# مدل CLIP
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# دیتابیس
client = chromadb.PersistentClient(path="./db")
collection = client.get_or_create_collection("fashion")

image_folder = "images"

for idx, img_name in enumerate(os.listdir(image_folder)):
    img_path = os.path.join(image_folder, img_name)

    image = Image.open(img_path).convert("RGB")

    inputs = processor(images=image, return_tensors="pt")

    with torch.no_grad():
        embedding = model.get_image_features(**inputs)

    vector = embedding[0].tolist()

    collection.add(
        ids=[str(idx)],
        embeddings=[vector],
        metadatas=[{"file": img_name}]
    )

    print(f"Added: {img_name}")

print("DONE")