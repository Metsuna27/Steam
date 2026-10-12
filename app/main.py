from fastapi import FastAPI, HTTPException, Query
from pymongo.errors import PyMongoError
from app.routers.games_router import router as games_router

from app.database import (
    games_collection,
    check_connection
)

app = FastAPI(
    title="Steam API",
    description="API REST pour la gestion des jeux Steam",
    version="1.0.0"
)

app.include_router(games_router)


@app.get("/health")
def health():
    if check_connection():
        return {
            "status": "ok",
            "database": "connected"
        }

    raise HTTPException(
        status_code=503,
        detail="MongoDB indisponible"
    )


@app.get("/api/v1/games")
def get_games(
    limit: int = Query(default=10, ge=1, le=100),
    skip: int = Query(default=0, ge=0)
):
    try:
        total = games_collection.count_documents({})

        cursor = (
            games_collection
            .find({}, {"_id": 0})
            .skip(skip)
            .limit(limit)
        )

        games = list(cursor)

        return {
            "items": games,
            "page": (skip // limit) + 1,
            "pageSize": limit,
            "totalItems": total,
            "totalPages": (total + limit - 1) // limit,
            "_links": {
                "self": (
                    f"/api/v1/games?limit={limit}&skip={skip}"
                ),
                "next": (
                    f"/api/v1/games?limit={limit}&skip={skip + limit}"
                    if skip + limit < total else None
                )
            }
        }

    except PyMongoError:
        raise HTTPException(
            status_code=503,
            detail="Erreur d'accès à MongoDB"
        )