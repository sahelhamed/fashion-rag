from transformers import CLIPModel, CLIPProcessor
from config import MODEL_NAME

model = CLIPModel.from_pretrained(MODEL_NAME)
processor = CLIPProcessor.from_pretrained(MODEL_NAME)