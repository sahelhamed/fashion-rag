from services.search import (
    search_by_text
)

from services.llm_stylist import (
    generate_style_advice
)

query = input(
    "Search: "
)

results = search_by_text(
    query,
    n_results=5
)

items = results["ids"][0]

print("\nResults:\n")

for item in items:
    print("-", item)

print(
    "\nGenerating style recommendation...\n"
)

answer = generate_style_advice(
    query,
    items
)

print(answer)