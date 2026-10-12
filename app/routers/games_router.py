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