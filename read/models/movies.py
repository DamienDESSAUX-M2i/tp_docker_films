from utils.genre import Genre


class Movie:
    ID: int = 0

    def __init__(self, titre: str, annee_production: int, genre: Genre, age_limite: int) -> None:
        """Constructor of the class Movie.

        Args:
            titre (str): Title of the movie.
            annee_production (int): Year of production of the movie.
            genre (str): Genre of the movie.
            age_limite (int): Age limit for the movie.
        """
        Movie.ID += 1
        self._titre: str = None
        self.titre = titre
        self._annee_production: int = None
        self.annee_production = annee_production
        self._genre: str = None
        self.genre = genre
        self._age_limite: int = None
        self.age_limite = age_limite
    
    @property
    def titre(self) -> str:
        return self._titre
    
    @titre.setter
    def titre(self, titre: str) -> None:
        if not isinstance(titre, str):
            raise TypeError('Type of titre must be str.')
        self._titre = titre
    
    @property
    def annee_production(self) -> int:
        return self._annee_production
    
    @annee_production.setter
    def annee_production(self, annee_production: int) -> None:
        if not isinstance(annee_production, int):
            raise TypeError('Type of annee_production must be int.')
        self._annee_production = annee_production
    
    @property
    def genre(self) -> Genre:
        return self._genre
    
    @genre.setter
    def genre(self, genre: Genre) -> None:
        if not isinstance(genre, Genre):
            raise TypeError('Type of genre must be an instance of class Genre.')
        self._genre = genre
    
    @property
    def age_limite(self) -> int:
        return self._age_limite
    
    @age_limite.setter
    def age_limite(self, age_limite: int) -> None:
        if not isinstance(age_limite, int):
            raise TypeError('Type of age_limite must be int.')
        self._age_limiten = age_limite
    
    def __str__(self) -> None:
        """Display attributs and values of the class."""
        infos: list[str] = ["=== Infos ==="]
        for attribut, value in self.__dict__.items():
            infos.append(f"{attribut} : {value}")
        return "\n".join(infos)