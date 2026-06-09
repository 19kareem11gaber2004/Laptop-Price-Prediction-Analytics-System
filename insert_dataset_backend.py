import os
import pandas as pd
from datetime import datetime, timezone
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv("backend/.env")

MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise ValueError("MONGO_URI not found in backend/.env")

client = MongoClient(MONGO_URI)
db = client["advanced_db_project"]   # نفس DB اللي شغال عندك
dataset_col = db["dataset"]

CSV_PATH = r"data\cleaned\cleaned_ebay_laptop_data.csv"
if not os.path.exists(CSV_PATH):
    raise FileNotFoundError(f"CSV not found: {CSV_PATH}")

df = pd.read_csv(CSV_PATH)

now = datetime.now(timezone.utc)
df["created_at"] = now
df["updated_at"] = now

records = df.to_dict(orient="records")

dataset_col.delete_many({})  # optional: clear old data
dataset_col.insert_many(records)

print("✅ Inserted rows:", len(records))
print("✅ dataset count now:", dataset_col.count_documents({}))
