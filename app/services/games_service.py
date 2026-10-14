from app.repositories.games_repository import delete_game
from app.repositories.games_repository import update_game, replace_game
import logging
from app.exceptions.game_exception import GameNotFoundError, InvalidGameDataError

logger = logging.getLogger(__name__)

def delete_game_service(game_id: int):

    game = delete_game(game_id)
    if game is None:
        raise GameNotFoundError(f"Game with ID {game_id} not found.")

    # Log
    logger.info("Game deleted: ID=%s, Title=%s", game["_id"], game["title"])

    return game

def update_game_service(game_id: int, update_data: dict):
    if not update_data:
        raise InvalidGameDataError("No data provided for update.")
    game = update_game(game_id, update_data)
    if game is None:
        raise GameNotFoundError(f"Game with ID {game_id} not found.")

    # Log
    logger.info("Game updated: ID=%s, Title=%s", game["_id"], game["title"])

    return game

def replace_game_service(game_id: int, replacement: dict):
    if not replacement:
        raise InvalidGameDataError("No data provided for replacement.")
    game = replace_game(game_id, replacement)
    if game is None:
        raise GameNotFoundError(f"Game with ID {game_id} not found.")

    # Log
    logger.info("Game replaced: ID=%s, Title=%s", game["_id"], game["title"])

    return game