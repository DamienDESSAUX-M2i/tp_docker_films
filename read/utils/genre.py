from enum import Enum


class Genre(Enum):
    DRAME = "Drame"
    CRIME = "Crime"
    ACTION = "Action"
    AVENTURE = "Aventure"
    COMEDIE = "Comédie"
    BIOGRAPHIE = "Biographie"
    FAMILLE = "Famille"
    ANIMATION = "Animation"

    @classmethod
    def get_values(cls) -> list[str]:
        values: list[str] = []
        for genre in list(cls):
            values.append(genre.value)
        return values
