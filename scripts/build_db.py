import os
from PIL import Image

from db.chroma_client import (
    get_collection
)

from services.embedder import (
    get_image_embedding
)

from services.classifier import (
    classify_image
)

collection = get_collection()

image_folder = "images"

for file in os.listdir(
    image_folder
):

    if not file.lower().endswith(
        (
            ".jpg",
            ".jpeg",
            ".png"
        )
    ):
        continue

    img_path = os.path.join(
        image_folder,
        file
    )

    image = Image.open(
        img_path
    ).convert("RGB")

    category = classify_image(
        image
    )

    embedding = get_image_embedding(
        img_path
    )

    collection.add(
        ids=[file],
        embeddings=[embedding],
        documents=[file],
        metadatas=[
            {
                "category": category
            }
        ]
    )

    print(
        f"Added: {file} -> {category}"
    )

print(
    "\nDB build completed"
)