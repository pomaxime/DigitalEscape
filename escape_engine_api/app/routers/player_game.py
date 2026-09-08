from fastapi import APIRouter

from ..domain.code_puzzle import CodePuzzle
from ..domain.room import Room

router = APIRouter()


puzzle_1 = CodePuzzle(
    id="puzzle_1",
    name="L'énigme de Véloci Ruben",
    description="Écrivez la signification de l'inscription RAWR."
        "<< Rawr, je suis Véloci Ruben le Raptor, j'ai très faim, beaucoup trop faim." 
        "But i'm going to wait before eating you, Rawr."
        "Rawr, je veux des côtes. >>",
    secret_code="Raptor Affamé Want Ribs",
    hints=[
        "Tout vous ai donné dans l'ordre des paroles de Véloci Ruben."
    ],
)


room_1 = Room(
    id="room_1",
    name="Le laboratoire de Véloci Ruben",
    description=(
        "Vous êtes enfermés dans un laboratoire rempli de machines étranges"
        "et de dinosaures enfermés."
        "Une inscription affiche RAWR."
        "Un Raptor s'approche de vous et vous regarde avec insistance."
        "Vous entrez dans une pièce avec un ordinateur et un cadenas."
        "Pour avancer vous devrez trouver la signification de 'RAWR'."
        "Pour cela aidez vous des instruction de Véloci Ruben"
        "Le raptor vous suit et essaie d'entrer, vous l'entendez parler."
        "<< Rawr, je suis Véloci Ruben le Raptor, j'ai très faim, beaucoup trop faim." 
        "But i'm going to wait before eating you."
        "Rawr, je veux des côtes. >>"
        "Et oui, dans ce jeu tout peut être bilingue."
    ),
    puzzles=[puzzle_1],
    time_limit=900,
)


rooms = [room_1]