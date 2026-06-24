from PIL import Image
import torch

from models.clip_model import (
    model,
    processor
)


def image_to_vector(image_path):
    image = Image.open(
        image_path
    ).convert("RGB")

    inputs = processor(
        images=image,
        return_tensors="pt"
    )

    with torch.no_grad():
        embedding = model.get_image_features(
            **inputs
        )

    return embedding[0].tolist()


def text_to_vector(text):
    inputs = processor(
        text=[text],
        return_tensors="pt",
        padding=True
    )

    with torch.no_grad():
        embedding = model.get_text_features(
            **inputs
        )

    return embedding[0].tolist()