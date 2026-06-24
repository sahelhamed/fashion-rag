from db.chroma_client import get_collection

collection = get_collection()

collection.delete()
print("DB cleared")