from fastapi import APIRouter, Query
from app.services.games_service import get_paginated_games
from app.handlers.game_handler import delete_game_handler, update_game_handler

from fastapi import Depends
from fastapi.security import HTTPBearer
from typing import Literal


security = HTTPBearer()



router = APIRouter(
    prefix="/api/v1/games",
    tags=["Games"],
    dependencies=[Depends(security)]
)


@router.get("")
def list_games(
    limit: int = Query(10, ge=1, le=100),
    skip: int = Query(0, ge=0),
    search: str | None = Query(None, max_length=100),
    sort_by: Literal["_id", "title"] = "_id",
    order: Literal["asc", "desc"] = "asc"
):
    return get_paginated_games(
        limit=limit,
        skip=skip,
        search=search,
        sort_by=sort_by,
        order=order
    )

@router.delete("/{game_id}")
def delete_game(game_id: int):
    return delete_game_handler(game_id)

@router.put("/{game_id}")
def update_game(game_id: int, update_data: dict):
    return update_game_handler(game_id, update_data)

