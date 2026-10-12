from app.database import games_collection

def delete_game(game_id: int) -> bool:
    
    result = games_collection.delete_one({"_id": game_id})
    return result.deleted_count > 0
