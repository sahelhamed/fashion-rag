from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("ARVAN_ENDPOINT"))
print(os.getenv("ARVAN_API_KEY"))