from app.database import games_collection

def find_games(limit: int, skip: int):
    return list(
        games_collection.find({})
        .sort("_id", 1)
        .skip(skip)
        .limit(limit)
    )


def count_games():
    return games_collection.count_documents({})

def delete_game(game_id: int) -> bool:
    
    game = games_collection.find_one_and_delete({"_id": game_id})
    return game

