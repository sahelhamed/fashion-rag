from db import get_collection

collection = get_collection()

all_items = collection.get()

print("\nAvailable items:\n")

for item in all_items["ids"]:
    print("-", item)

selected = input("\nSelect item: ")

# پیدا کردن آیتم انتخاب شده
selected_item = collection.get(ids=[selected])

if not selected_item["ids"]:
    print("Item not found!")
    exit()

category = selected_item["metadatas"][0]["category"]

print("\nDetected category:", category)

def get_by_category(cat):
    return collection.get(where={"category": cat})

tops = get_by_category("top")
shirts = get_by_category("shirt")
shoes = get_by_category("shoes")
bottoms = get_by_category("bottom")

print("\n🎀 Style Suggestion\n")

print("Selected:")
print("-", selected)

if category == "shoes":
    print("\nTops:")
    for t in tops["documents"]:
        print("-", t)

    print("\nShirts:")
    for s in shirts["documents"]:
        print("-", s)

elif category == "top":
    print("\nShoes:")
    for s in shoes["documents"]:
        print("-", s)

    print("\nBottoms:")
    for b in bottoms["documents"]:
        print("-", b)

elif category == "bottom":
    print("\nTops:")
    for t in tops["documents"]:
        print("-", t)

    print("\nShoes:")
    for s in shoes["documents"]:
        print("-", s)