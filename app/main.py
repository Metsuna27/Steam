from fastapi import FastAPI, HTTPException

from app.database import check_connection
from app.routers.games_router import router as games_router

from pathlib import Path
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Steam API",
    description="API REST pour la gestion des jeux Steam",
    version="1.0.0"
)

FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"

app.mount(
    "/static",
    StaticFiles(directory=FRONTEND_DIR),
    name="static"
)

@app.get("/", include_in_schema=False)
def homepage():
    return FileResponse(FRONTEND_DIR / "index.html")


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