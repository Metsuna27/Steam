from app.database import users_collection


def find_user_by_email(email: str):
    return users_collection.find_one({"email": email})


def create_user(user: dict):
    result = users_collection.insert_one(user)
    return str(result.inserted_id)