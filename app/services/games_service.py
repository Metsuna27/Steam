from app.repositories.games_repository import delete_game

def delete_game_service(game_id: int):

    deleted = delete_game(game_id)
    if not deleted:
        raise ValueError(f"Game with ID {game_id} not found.")