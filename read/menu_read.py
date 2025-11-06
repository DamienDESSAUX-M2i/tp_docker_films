from pathlib import Path

from models.movies import Movie
import read_data
from exceptions.invalid_id_exception import InvalidIdException
from exceptions.invalid_title_exception import InvalidTitleException
from exceptions.invalid_age_limit_exception import InvalidAgeLimitException
from exceptions.invalid_genre_exception import InvalidGenreException
from exceptions.invalid_year_exception import InvalidYearException


class MenuRead:
    def __init__(self, file_path: Path):
        self.file_path = file_path
    
    def user_input_title(self) -> str:
        user_input: str = input("Titre : ").capitalize()
        if user_input.isalpha():
            return user_input
        raise InvalidTitleException("Un titre ne peut contenir que des caractères alphabétiques.")

    def user_input_annee_production(self) -> int:
        user_input: str = input("Année de production : ")
        if user_input.isdigit():
            return int(user_input)
        raise InvalidAgeLimitException("L'année de production doit être un nombre entier.")

    def user_input_genre(self) -> str:
        user_input: str = input("Genre : ").capitalize()
        if user_input.isalpha():
            return user_input
        raise InvalidGenreException("Le genre ne peut contenir que des caractères alphabétiques.")

    def user_input_age_limit(self) -> int:
        user_input: str = input("Age limite : ")
        if user_input.isdigit():
            return int(user_input)
        raise InvalidYearException("L'âge doit être un nombre entier.")

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

    def show_annee_production(self) -> int:
        while True:
            try:
                annee_production = self.user_input_annee_production()
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
                user_input: str = input("[1] Chercher un film par son titre\n[2] Chercher un film par limite d'âge\n[3] Chercher un film par son genre\n[4] Chercher un film par son année de production\n[0] Quitter\n=> ")
                match user_input:
                    case "1":
                        titre = self.show_title()
                        movies_accepted: list[Movie] = read_data.get_movies_title(file_path=self.file_path, titre=titre)
                        for movie in movies_accepted:
                            print(movie)
                    case "2":
                        age_limit = self.show_age_limit()
                        movies_accepted: list[Movie] = read_data.get_movies_age_limit(file_path=self.file_path, age_limite=age_limit)
                        for movie in movies_accepted:
                            print(movie)
                    case "3":
                        genre = self.show_genre()
                        movies_accepted: list[Movie] = read_data.get_movies_genre(file_path=self.file_path, genre=genre)
                        for movie in movies_accepted:
                            print(movie)
                    case "4":
                        annee_production1 = self.show_annee_production()
                        annee_production2 = self.show_annee_production()
                        movies_accepted: list[Movie] = read_data.get_movies_annees_production(file_path=self.file_path, annee_production1=annee_production1, annee_production2=annee_production2)
                        for movie in movies_accepted:
                            print(movie)
                    case "0":
                        break
                    case _:
                        raise ValueError("Erreur de saisie. Veuillez recommencer.")
            except ValueError as e:
                print(e)