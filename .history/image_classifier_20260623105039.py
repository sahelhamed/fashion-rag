from transformers import CLIPProcessor, CLIPModel
from PIL import Image

model = CLIPModel.from_pretrained(
    "openai/clip-vit-base-patch32"
)

processor = CLIPProcessor.from_pretrained(
    "openai/clip-vit-base-patch32"
)

image = Image.open("images/black_skirt.jpg")

inputs = processor(
    images=image,
    return_tensors="pt"
)

image_features = model.get_image_features(**inputs)

print(image_features.shape)