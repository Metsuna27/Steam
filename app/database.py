import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb://localhost:27017/"
)

MONGO_DB = os.getenv("MONGO_DB", "Steam")

client = MongoClient(
    MONGO_URI,
    serverSelectionTimeoutMS=5000
)
    
db = client[MONGO_DB]

games_collection = db["Game"]


def check_connection():
    try:
        client.admin.command("ping")
        return True
    except Exception:
        return False
        