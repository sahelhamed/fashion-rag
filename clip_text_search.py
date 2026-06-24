from transformers import CLIPProcessor, CLIPModel
import torch
import chromadb

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

collection = client.get_collection(
    "fashion_clip"
)

# -----------------------
# USER QUERY (TEXT)
# -----------------------
query_text = input("Search (text): ")

# -----------------------
# TEXT → EMBEDDING
# -----------------------
inputs = processor(
    text=[query_text],
    return_tensors="pt",
    padding=True
)

with torch.no_grad():
    text_embedding = model.get_text_features(
        **inputs
    )

# -----------------------
# SEARCH
# -----------------------
results = collection.query(
    query_embeddings=[
        text_embedding[0].tolist()
    ],
    n_results=3
)

# -----------------------
# OUTPUT
# -----------------------
print("\nResults:\n")

for item in results["ids"][0]:
    print("-", item)