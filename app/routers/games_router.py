from fastapi import APIRouter, Query
from app.services.games_service import get_paginated_games
from app.handlers.game_handler import delete_game_handler, update_game_handler

router = APIRouter(
    prefix="/api/v1/games",
    tags=["Games"]
)


@router.get("")
def list_games(
    limit: int = Query(10, ge=1, le=100),
    skip: int = Query(0, ge=0)
):
    return get_paginated_games(limit, skip)

@router.delete("/api/v1/games/{game_id}")
def delete_game(game_id: int):
    return delete_game_handler(game_id)

@router.put("/api/v1/games/{game_id}")
def update_game(game_id: int, update_data: dict):
    return update_game_handler(game_id, update_data)

