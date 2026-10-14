from app.database import games_collection

def delete_game(game_id: int) -> bool:
    
    game = games_collection.find_one_and_delete({"_id": game_id})
    return game
