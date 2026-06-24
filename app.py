from services.embedder import (
    text_to_vector
)

from services.search import (
    search_by_vector
)

query = input(
    "Search: "
)

vector = text_to_vector(
    query
)

results = search_by_vector(
    vector
)

print("\nResults:\n")

for item in results["ids"][0]:
    print("-", item)