from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch
import chromadb

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

client = chromadb.PersistentClient(path="./db")
collection = client.get_collection("fashion")

query_image = Image.open("images/black_skirt.jpg").convert("RGB")

inputs = processor(images=query_image, return_tensors="pt")

with torch.no_grad():
    query_embedding = model.get_image_features(**inputs)

results = collection.query(
    query_embeddings=[query_embedding[0].tolist()],
    n_results=3
)

print(results)