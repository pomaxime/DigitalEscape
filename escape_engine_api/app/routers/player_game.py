from fastapi import APIRouter

from app.domain.room import Room
from app.domain.code_puzzle import CodePuzzle


router = APIRouter()


puzzle_1 = CodePuzzle(
    id="puzzle_1",
    name="L'énigme de Vélocie Ruben",
    description=""
    "écrire l'énigme ici",
    secret_code="Raptor Affamé Want Ribs"
)


room_1 = Room(
    id="room_1",
    name="Le laboratoire de Vélocie Ruben",
    description=(
        "Vous êtes enfermés dans le laboratoire du raptor "
        "Vélocie Ruben. Une inscription affiche RAWR. "
        "Vous devez découvrir sa signification pour continuer."
    ),
    puzzles=[puzzle_1]
)


rooms = [room_1]