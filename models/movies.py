class Movie:
    ID: int = 0

    def __init__(self, titre: str, annee_production: int, genre: str, age_limite: int) -> None:
        """Constructor of the class Movie.

        Args:
            titre (str): Title of the movie.
            annee_production (int): Year of production of the movie.
            genre (str): Genre of the movie.
            age_limite (int): Age limit for the movie.
        """
        Movie.ID += 1
        self.titre: str = titre
        self.annee_production: int = annee_production
        self.genre: str = genre
        self.age_limite: int = age_limite
    
    def __str__(self) -> None:
        """Display attributs and values of the class."""
        infos: list[str] = ["=== Infos ==="]
        for attribut, value in self.__dict__.items():
            infos.append(f"{attribut} : {value}")
        return "\n".join(infos)