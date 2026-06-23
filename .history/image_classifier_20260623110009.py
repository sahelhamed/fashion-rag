from transformers import pipeline

classifier = pipeline(
    "image-classification",
    model="google/vit-base-patch16-224"
)

result = classifier("images/black_skirt.jpg")

print(result[:5])