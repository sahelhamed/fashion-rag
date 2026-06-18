import chromadb
from sentence_transformers import SentenceTransformer

# =========================
# 1. Model
# =========================
model = SentenceTransformer("all-MiniLM-L6-v2")

# =========================
# 2. DB
# =========================
client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_collection("clothes")

# =========================
# 3. USER INPUT (مرحله جدید)
# =========================
query = "white skirt outfit"

# =========================
# 4. RETRIEVAL (RAG core)
# =========================
results = collection.query(
    query_texts=[query],
    n_results=3
)

docs = results["documents"][0]

# =========================
# 5. STYLE ENGINE (قدم جدید)
# =========================
print("\n🎀 پیشنهاد استایل برای شما:\n")

if len(docs) > 0:
    # ساده‌ترین استایلر (فعلاً rule-based)
    outfit = []

    # دامن / آیتم اصلی فرض می‌کنیم
    outfit.append(query)

    # آیتم‌های پیشنهادی از DB
    for d in docs:
        if "shoe" in d:
            outfit.append(d + " 👟")
        elif "shirt" in d or "top" in d:
            outfit.append(d + " 👕")
        else:
            outfit.append(d)

    print("👉 ترکیب پیشنهادی:")
    for item in outfit:
        print("-", item)

else:
    print("هیچ آیتم مرتبطی پیدا نشد 😕")