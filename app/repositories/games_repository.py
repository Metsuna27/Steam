from app.database import games_collection
from pymongo import ReturnDocument

def delete_game(game_id: int) -> bool: 
    
    game = games_collection.find_one_and_delete({"_id": game_id})
    return game

def replace_game(game_id: int, replacement: dict):
    game = games_collection.find_one_and_replace(
        {"_id": game_id},
        replacement,
        return_document=ReturnDocument.AFTER
    )
    return game

def update_game(game_id: int, update_data: dict):
    result = games_collection.find_one_and_update(
        {"_id": game_id},
        {"$set": update_data},
        return_document=ReturnDocument.AFTER
    )
    return result