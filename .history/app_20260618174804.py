selected = input("Select item: ")

selected_item = collection.get(where={"id": selected})

category = selected_item["metadatas"][0]["category"]

print("\nDetected category:", category)

def get_by_category(cat):
    return collection.get(
        where={"category": cat}
    )

tops = get_by_category("top")
shirts = get_by_category("shirt")
shoes = get_by_category("shoes")
bottoms = get_by_category("skirt")

print("\nStyle Suggestion\n")

print("Selected:")
print("-", selected)

if category == "shoes":
    print("\nTops:")
    for t in tops["documents"]:
        print("-", t)

    print("\nShirts:")
    for s in shirts["documents"]:
        print("-", s)