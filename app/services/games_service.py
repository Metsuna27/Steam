from urllib.parse import urlencode
import logging

from app.repositories.games_repository import (
    find_games,
    count_games,
    delete_game,
    update_game
)

logger = logging.getLogger(__name__)


def get_paginated_games(
    limit: int,
    skip: int,
    search: str | None = None,
    sort_by: str = "_id",
    order: str = "asc"
):
    # Récupération des jeux filtrés et triés
    games = find_games(
        limit=limit,
        skip=skip,
        search=search,
        sort_by=sort_by,
        order=order
    )

    # Nombre total de jeux correspondant à la recherche
    total = count_games(search)

    # Pagination
    page = (skip // limit) + 1
    total_pages = (total + limit - 1) // limit

    # Construction des liens de pagination
    def build_link(offset: int):
        params = {
            "limit": limit,
            "skip": offset,
            "sort_by": sort_by,
            "order": order
        }

        if search:
            params["search"] = search

        return "/api/v1/games?" + urlencode(params)

    return {
        "items": games,
        "page": page,
        "pageSize": limit,
        "totalItems": total,
        "totalPages": total_pages,
        "_links": {
            "self": build_link(skip),
            "next": (
                build_link(skip + limit)
                if skip + limit < total else None
            ),
            "previous": (
                build_link(max(0, skip - limit))
                if skip > 0 else None
            )
        }
    }


def delete_game_service(game_id: int):
    game = delete_game(game_id)

    if game is None:
        raise ValueError(
            f"Game with ID {game_id} not found."
        )

    logger.info(
        "Game deleted: ID=%s, Title=%s",
        game["_id"],
        game.get("title")
    )

    return game


def update_game_service(game_id: int, update_data: dict):
    game = update_game(game_id, update_data)

    if game is None:
        raise ValueError(
            f"Game with ID {game_id} not found."
        )

    logger.info(
        "Game updated: ID=%s, Title=%s",
        game["_id"],
        game.get("title")
    )

    return game