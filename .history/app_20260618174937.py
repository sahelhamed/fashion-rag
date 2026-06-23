import chromadb

# 1. connect to vector db
client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection(name="clothes")

# 2. input
selected = input("Select item: ")

# 3. find selected item
selected_item = collection.get(where={"id": selected})

if len(selected_item["ids"]) == 0:
    print("Item not found!")
    exit()

category = selected_item["metadatas"][0]["category"]

print("\nDetected category:", category)

# 4. helper
def get_by_category(cat):
    return collection.get(where={"category": cat})

tops = get_by_category("top")
shirts = get_by_category("shirt")
shoes = get_by_category("shoes")
bottoms = get_by_category("skirt")

# 5. output
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