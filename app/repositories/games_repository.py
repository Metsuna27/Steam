
import re

from app.database import games_collection
from pymongo import ReturnDocument


def build_game_filter(search: str | None = None):
    filters = {}

    if search:
        filters["title"] = {
            "$regex": re.escape(search),
            "$options": "i"
        }

    return filters


def find_games(
    limit: int,
    skip: int,
    search: str | None = None,
    sort_by: str = "_id",
    order: str = "asc"
):
    filters = build_game_filter(search)

    sort_direction = 1 if order == "asc" else -1

    sort_fields = [(sort_by, sort_direction)]

    if sort_by != "_id":
        sort_fields.append(("_id", 1))

    return list(
        games_collection
        .find(filters)
        .sort(sort_fields)
        .skip(skip)
        .limit(limit)
    )


def count_games(search: str | None = None):
    filters = build_game_filter(search)

    return games_collection.count_documents(filters)


def delete_game(game_id: int):
    return games_collection.find_one_and_delete(
        {"_id": game_id}
    )


def update_game(game_id: int, update_data: dict):
    return games_collection.find_one_and_update(
        {"_id": game_id},
        {"$set": update_data},
        return_document=ReturnDocument.AFTER
    )
