from fastapi import HTTPException
from app.services.games_service import delete_game_service

def delete_game_handler(game_id: int):
    try:
        game =delete_game_service(game_id)
        return {
            "message": "Game deleted successfully",
            "id": game["_id"],
            "title": game["title"]
        }
    
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))