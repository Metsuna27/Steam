<<<<<<< HEAD
from fastapi import APIRouter, Query
from app.services.games_service import get_paginated_games

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
=======
from fastapi import APIRouter
from app.handlers.game_handler import delete_game_handler

router = APIRouter()

@router.delete("/api/v1/games/{game_id}")
def delete_game(game_id: int):
    return delete_game_handler(game_id)
>>>>>>> 930c7d9c11b110a53085aee65188abd905182d1a
