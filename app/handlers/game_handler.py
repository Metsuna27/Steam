from fastapi import HTTPException
from app.services.games_service import delete_game_service, update_game_service, replace_game_service
from app.exceptions.game_exception import GameNotFoundError, InvalidGameDataError

def delete_game_handler(game_id: int):
    try:
        game =delete_game_service(game_id)
        return {
            "message": "Game deleted successfully",
            "id": game["_id"],
            "title": game["title"]
        }
    
    except GameNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

def update_game_handler(game_id: int, update_data: dict):
    try:
        game = update_game_service(game_id, update_data)
        return {
            "message": "Game updated successfully",
            "id": game["_id"],
            "title": game["title"]
        }

    except InvalidGameDataError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except GameNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


def replace_game_handler(game_id: int, replacement: dict):
    try:
        game = replace_game_service(game_id, replacement)
        return {
            "message": "Game replaced successfully",
            "id": game["_id"],
            "title": game["title"]
        }

    except InvalidGameDataError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except GameNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))