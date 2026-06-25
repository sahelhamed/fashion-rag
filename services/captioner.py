from PIL import Image

from models.caption_model import (
    processor,
    model
)


def generate_caption(image_path):
    image = Image.open(
        image_path
    ).convert("RGB")

    inputs = processor(
        image,
        return_tensors="pt"
    )

    output = model.generate(
        **inputs,
        max_new_tokens=30
    )

    caption = processor.decode(
        output[0],
        skip_special_tokens=True
    )

    return caption