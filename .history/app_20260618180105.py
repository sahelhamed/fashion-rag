from db import get_collection

# =========================
# 1. اتصال به DB
# =========================
collection = get_collection()

# =========================
# 2. ورودی کاربر
# =========================
selected = input("Select item: ")

# =========================
# 3. RAG search
# =========================
results = collection.query(
    query_texts=[selected],
    n_results=1
)

if len(results["ids"][0]) == 0:
    print("Item not found!")
    exit()

selected_doc = results["documents"][0][0]
selected_meta = results["metadatas"][0][0]

category = selected_meta.get("category", "unknown")

print("\nDetected category:", category)

# =========================
# 4. helper function
# =========================
def get_by_category(cat):
    return collection.get(where={"category": cat})

tops = get_by_category("top")
shirts = get_by_category("shirt")
shoes = get_by_category("shoes")
bottoms = get_by_category("skirt")

# =========================
# 5. output
# =========================
print("\nStyle Suggestion\n")

print("Selected:")
print("-", selected_doc)

if category == "shoes":
    print("\nTops:")
    for t in tops["documents"]:
        print("-", t)

    print("\nShirts:")
    for s in shirts["documents"]:
        print("-", s)

elif category in ["top", "shirt"]:
    print("\nBottoms:")
    for b in bottoms["documents"]:
        print("-", b)

    print("\nShoes:")
    for s in shoes["documents"]:
        print("-", s)

elif category == "skirt":
    print("\nTops:")
    for t in tops["documents"]:
        print("-", t)

    print("\nShoes:")
    for s in shoes["documents"]:
        print("-", s)