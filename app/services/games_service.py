from app.repositories.games_repository import delete_game
import logging

logger = logging.getLogger(__name__)

def delete_game_service(game_id: int):

    game = delete_game(game_id)
    if game is None:
        raise ValueError(f"Game with ID {game_id} not found.")

    # Log
    logger.info(f"Game deleted: ID=%s, Title=%s", game["_id"], game["title"])

    return game


