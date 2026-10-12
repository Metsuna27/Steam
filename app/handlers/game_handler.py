from fastapi import HTTPException
from app.services.games_service import delete_game_service

def delete_game_handler(game_id: int):
    try:
        delete_game_service(game_id)
        return {"message": f"Game with ID {game_id} deleted successfully."}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))