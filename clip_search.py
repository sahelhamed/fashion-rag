from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch
import chromadb

model = CLIPModel.from_pretrained(
    "openai/clip-vit-base-patch32"
)

processor = CLIPProcessor.from_pretrained(
    "openai/clip-vit-base-patch32"
)

client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_collection(
    "fashion_clip"
)

query_image = Image.open(
    "images/black_skirt.jpg"
).convert("RGB")

inputs = processor(
    images=query_image,
    return_tensors="pt"
)

with torch.no_grad():
    embedding = model.get_image_features(
        **inputs
    )

results = collection.query(
    query_embeddings=[
        embedding[0].tolist()
    ],
    n_results=3
)

print("\nMost Similar Items:\n")

for item in results["ids"][0]:
    print("-", item)