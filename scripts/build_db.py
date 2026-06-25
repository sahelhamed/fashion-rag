import os

from db.chroma_client import get_collection

from services.embedder import (
    image_to_vector
)

from services.captioner import (
    generate_caption
)

collection = get_collection()

image_folder = "images"

for img_name in os.listdir(image_folder):

    if not img_name.lower().endswith(
        (".jpg", ".jpeg", ".png")
    ):
        continue

    image_path = os.path.join(
        image_folder,
        img_name
    )

    embedding = image_to_vector(
        image_path
    )

    caption = generate_caption(
        image_path
    )

    collection.add(
        ids=[img_name],
        embeddings=[embedding],
        documents=[caption],
        metadatas=[
            {
                "file": img_name
            }
        ]
    )

    print(f"Added: {img_name}")
    print(f"Caption: {caption}")

print("\nDB build completed.")