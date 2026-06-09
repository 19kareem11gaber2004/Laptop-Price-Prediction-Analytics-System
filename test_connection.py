from pymongo import MongoClient
from dotenv import load_dotenv
import os

# تحميل متغيرات البيئة
load_dotenv()

# قراءة الـ URI
MONGO_URI = os.getenv("MONGO_URI")

# الاتصال بـ MongoDB
client = MongoClient(MONGO_URI)

# إنشاء / اختيار Database
db = client["advanced_db"]

# اختبار الاتصال
print("Databases available:")
print(client.list_database_names())

print("✅ Connected to MongoDB Atlas successfully!")
