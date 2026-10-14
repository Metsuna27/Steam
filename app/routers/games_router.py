from fastapi import APIRouter
from app.handlers.game_handler import delete_game_handler, update_game_handler, replace_game_handler
from app.models.game_model import GamePatch, GameReplace

router = APIRouter()

@router.delete("/api/v1/games/{game_id}")
def delete_game(game_id: int):
    return delete_game_handler(game_id)

@router.patch("/api/v1/games/{game_id}")
def update_game(game_id: int, game_patch: GamePatch):
    update_data = game_patch.model_dump(exclude_unset=True)
    return update_game_handler(game_id, update_data)

@router.put("/api/v1/games/{game_id}")
def replace_game(game_id: int, game_replace: GameReplace):
    replacement = game_replace.model_dump()
    return replace_game_handler(game_id, replacement)