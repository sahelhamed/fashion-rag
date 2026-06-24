from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch

MODEL_NAME = "openai/clip-vit-base-patch32"

model = CLIPModel.from_pretrained(
    MODEL_NAME
)

processor = CLIPProcessor.from_pretrained(
    MODEL_NAME
)

CATEGORIES = [
    "shirt",
    "t-shirt",
    "top",
    "skirt",
    "pants",
    "jeans",
    "sneakers",
    "boots",
    "dress"
]


def classify_image(
    image: Image.Image
) -> str:

    inputs = processor(
        text=CATEGORIES,
        images=image,
        return_tensors="pt",
        padding=True
    )

    with torch.no_grad():

        outputs = model(
            **inputs
        )

        logits = outputs.logits_per_image

        probs = logits.softmax(
            dim=1
        )

    best_idx = probs.argmax().item()

    return CATEGORIES[
        best_idx
    ]