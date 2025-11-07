from pathlib import Path

from models.movies import Movie
from utils.genre import Genre
import read_data
from exceptions.invalid_id_exception import InvalidIdException
from exceptions.invalid_title_exception import InvalidTitleException
from exceptions.invalid_age_limit_exception import InvalidAgeLimitException
from exceptions.invalid_signal_exception import InvalidSignalException
from exceptions.invalid_genre_exception import InvalidGenreException
from exceptions.invalid_year_exception import InvalidYearException


class MenuRead:
    def __init__(self, file_path: Path):
        self.file_path = file_path

    def user_input_title(self) -> str:
        return input("Titre : ").title()

    def user_input_annee_production(self, msg: str, born_inf: int) -> int:
        if type(born_inf) is not int:
            raise TypeError("The type of born_inf must be int.")
        user_input: str = input(msg)
        if user_input.isdigit():
            user_input: int = int(user_input)
            if user_input >= born_inf:
                return user_input
        raise InvalidAgeLimitException(
            f"L'année de production doit être un nombre entier supérieur ou égal à {born_inf}."
        )

    def user_input_genre(self) -> str:
        user_input: str = input("Genre : ").title()
        if user_input in Genre.get_values():
            return Genre(user_input)
        raise InvalidGenreException(
            f"Le genre {user_input} n'est pas valide.\nLa liste des genres valide est : {', '.join(Genre.get_values())}."
        )

    def user_input_age_limit(self) -> int:
        user_input: str = input("Age limite : ")
        if user_input.isdigit():
            user_input: int = int(user_input)
            if user_input >= 0:
                return user_input
        raise InvalidYearException("L'âge doit être un nombre entier positif.")

    def show_id(self) -> int:
        while True:
            try:
                id = self.user_input_id()
                return id
            except InvalidIdException as e:
                e.display_message_error()

    def show_title(self) -> str:
        while True:
            try:
                titre = self.user_input_title()
                return titre
            except InvalidTitleException as e:
                e.display_message_error()

    def show_annee_production(self, msg: str, born_inf: int = 0) -> int:
        while True:
            try:
                annee_production = self.user_input_annee_production(msg, born_inf)
                return annee_production
            except InvalidAgeLimitException as e:
                e.display_message_error()

    def show_genre(self) -> str:
        while True:
            try:
                genre = self.user_input_genre()
                return genre
            except InvalidGenreException as e:
                e.display_message_error()

    def show_age_limit(self) -> int:
        while True:
            try:
                age_limit = self.user_input_age_limit()
                return age_limit
            except InvalidYearException as e:
                e.display_message_error()

    def show(self):
        while True:
            try:
                user_input: str = input(
                    "[1] Chercher un film par son titre\n[2] Chercher un film par limite d'âge\n[3] Chercher un film par son genre\n[4] Chercher un film par son année de production\n[0] Quitter\n=> "
                )
                match user_input:
                    case "1":
                        titre: str = self.show_title()
                        movies: list[Movie] = read_data.get_movies_title(
                            file_path=self.file_path, titre=titre
                        )
                        for movie in movies:
                            print(movie)
                    case "2":
                        age_limit: int = self.show_age_limit()
                        movies: list[Movie] = read_data.get_movies_age_limit(
                            file_path=self.file_path, age_limite=age_limit
                        )
                        for movie in movies:
                            print(movie)
                    case "3":
                        genre: Genre = self.show_genre()
                        movies: list[Movie] = read_data.get_movies_genre(
                            file_path=self.file_path, genre=genre
                        )
                        for movie in movies:
                            print(movie)
                    case "4":
                        annee_production1: int = self.show_annee_production(
                            "Année de production (borne inférieure) : "
                        )
                        annee_production2: int = self.show_annee_production(
                            "Année de production (borne suppérieure) : ",
                            annee_production1,
                        )
                        movies: list[Movie] = read_data.get_movies_annees_production(
                            file_path=self.file_path,
                            annee_production1=annee_production1,
                            annee_production2=annee_production2,
                        )
                        for movie in movies:
                            print(movie)
                    case "0":
                        break
                    case _:
                        raise InvalidSignalException(
                            "Erreur de saisie. Veuillez recommencer."
                        )
            except InvalidSignalException as e:
                e.display_message_error()
