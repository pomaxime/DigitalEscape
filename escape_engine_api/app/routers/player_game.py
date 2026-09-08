from fastapi import APIRouter

from ..domain.code_puzzle import CodePuzzle
from ..domain.room import Room

router = APIRouter()


puzzle_1 = CodePuzzle(
    id="puzzle_1",
    name="L'énigme de Vélocie Ruben",
    description="Écrivez la signification de l'inscription RAWR.",
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