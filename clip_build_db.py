from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch
import chromadb
import os

# -----------------------
# MODEL
# -----------------------
model = CLIPModel.from_pretrained(
    "openai/clip-vit-base-patch32"
)

processor = CLIPProcessor.from_pretrained(
    "openai/clip-vit-base-patch32"
)

# -----------------------
# DB
# -----------------------
client = chromadb.PersistentClient(
    path="chroma_db"
)

# پاک کردن کالکشن قبلی
try:
    client.delete_collection("fashion_clip")
except:
    pass

collection = client.get_or_create_collection(
    name="fashion_clip"
)

image_folder = "images"


def get_embedding(image_path):
    image = Image.open(image_path).convert("RGB")

    inputs = processor(
        images=image,
        return_tensors="pt"
    )

    with torch.no_grad():
        embedding = model.get_image_features(
            **inputs
        )

    return embedding[0].tolist()


# -----------------------
# BUILD DATABASE
# -----------------------
for img_name in os.listdir(image_folder):

    if not img_name.lower().endswith(
        (".jpg", ".jpeg", ".png")
    ):
        continue

    img_path = os.path.join(
        image_folder,
        img_name
    )

    vector = get_embedding(img_path)

    collection.add(
        ids=[img_name],
        embeddings=[vector],
        metadatas=[
            {
                "file": img_name
            }
        ]
    )

    print("Added:", img_name)

print("\nDONE: CLIP DB built")