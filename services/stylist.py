from db.chroma_client import get_collection

collection = get_collection()

def get_by_category(cat):
    return collection.get(where={"category": cat})


def detect_category(meta):
    return meta.get("category", "unknown")


def suggest_outfit(category):
    tops = get_by_category("top")
    shirts = get_by_category("shirt")
    shoes = get_by_category("shoes")
    bottoms = get_by_category("bottom")

    print("\n🎀 Style Suggestion\n")

    if category == "bottom":
        print("Tops:")
        for t in tops["documents"]:
            print("-", t)

        print("\nShoes:")
        for s in shoes["documents"]:
            print("-", s)

    elif category == "top":
        print("Bottoms:")
        for b in bottoms["documents"]:
            print("-", b)

        print("\nShoes:")
        for s in shoes["documents"]:
            print("-", s)

    elif category == "shoes":
        print("Tops:")
        for t in tops["documents"]:
            print("-", t)

        print("\nBottoms:")
        for b in bottoms["documents"]:
            print("-", b)