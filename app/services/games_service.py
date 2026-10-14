from app.repositories.games_repository import delete_game
from app.repositories.games_repository import update_game
import logging

logger = logging.getLogger(__name__)

def delete_game_service(game_id: int):

    game = delete_game(game_id)
    if game is None:
        raise ValueError(f"Game with ID {game_id} not found.")

    # Log
    logger.info("Game deleted: ID=%s, Title=%s", game["_id"], game["title"])

    return game

def update_game_service(game_id: int, update_data: dict):
    game = update_game(game_id, update_data)
    if game is None:
        raise ValueError(f"Game with ID {game_id} not found.")

    # Log
    logger.info("Game updated: ID=%s, Title=%s", game["_id"], game["title"])

    return game
