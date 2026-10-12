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