from services.embedder import image_to_vector
from services.search import search

img = "images/black_skirt.jpg"

vector = image_to_vector(img)

results = search(vector)

print("\nMost Similar Items:\n")

for item in results["ids"][0]:
    print("-", item)