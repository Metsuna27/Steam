from fastapi import APIRouter
from app.handlers.game_handler import delete_game_handler, update_game_handler

router = APIRouter()

@router.delete("/api/v1/games/{game_id}")
def delete_game(game_id: int):
    return delete_game_handler(game_id)

@router.put("/api/v1/games/{game_id}")
def update_game(game_id: int, update_data: dict):
    return update_game_handler(game_id, update_data)