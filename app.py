from services.search import (
    search_by_text
)

query = input(
    "Search: "
)

results = search_by_text(
    query
)

print("\nResults:\n")

for item in results["ids"][0]:
    print("-", item)