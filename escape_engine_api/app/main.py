from fastapi import FastAPI

from .routers.player_game import router as player_game_router

app = FastAPI()
app.include_router(player_game_router)

@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API pour mon super escape game!"}

rooms = {
    "room1": {"name": "Room 1", "description": "This is room 1"},
    "room2": {"name": "Room 2", "description": "This is room 2"}
}

@app.get("/room")
def get_rooms():
    return list(rooms.keys())

@app.get("/room/{room_id}")
def get_room(room_id: str):
    return rooms.get(room_id)

# Lancer le serveur depuis le terminal :
# fastapi dev exemple_3.py
