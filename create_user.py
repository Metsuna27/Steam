from dotenv import load_dotenv
from pwdlib import PasswordHash
from pymongo.errors import DuplicateKeyError

load_dotenv()

from app.database import users_collection

password_hash = PasswordHash.recommended()

email = "admin@steam.com"
password = "Admin123456!"

user = {
    "email": email,
    "password": password_hash.hash(password),
    "role": "admin"
}

try:
    result = users_collection.insert_one(user)
    print("Utilisateur créé :", result.inserted_id)

except DuplicateKeyError:
    print("Cet utilisateur existe déjà.")