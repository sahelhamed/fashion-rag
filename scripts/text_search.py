from services.embedder import text_to_vector
from services.search import search

query = input("Search text: ")

vector = text_to_vector(query)

results = search(vector)

print("\nResults:\n")

for item in results["ids"][0]:
    print("-", item)