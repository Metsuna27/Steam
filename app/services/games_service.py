from app.repositories.games_repository import find_games, count_games


def get_paginated_games(limit: int, skip: int):
    games = find_games(limit, skip)
    total = count_games()

    page = (skip // limit) + 1
    total_pages = (total + limit - 1) // limit

    return {
        "items": games,
        "page": page,
        "pageSize": limit,
        "totalItems": total,
        "totalPages": total_pages,
        "_links": {
            "self": f"/api/v1/games?limit={limit}&skip={skip}",
            "next": (
                f"/api/v1/games?limit={limit}&skip={skip + limit}"
                if skip + limit < total else None
            ),
            "previous": (
                f"/api/v1/games?limit={limit}&skip={max(0, skip - limit)}"
                if skip > 0 else None
            )
        }
    }