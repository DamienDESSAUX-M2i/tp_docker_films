from pathlib import Path

from models.movies import Movie
import manip_data as manip_data
from exceptions.invalid_id_exception import InvalidIdException
from exceptions.invalid_title_exception import InvalidTitleException
from exceptions.invalid_age_limit_exception import InvalidAgeLimitException
from exceptions.invalid_signal_exception import InvalidSignalException
from exceptions.invalid_genre_exception import InvalidGenreException
from exceptions.invalid_year_exception import InvalidYearException


class MenuWrite:
    def __init__(self, file_path: Path):
        self.file_path = file_path

    def user_input_id(self) -> str:
        user_input: str = input("Id : ").capitalize()
        if user_input.isdigit():
            user_input = int(user_input)
            if 1 <= user_input <= Movie.ID:
                return user_input
        raise InvalidTitleException(f"L'identifiant doit être un nombre entier compris entre 1 et {Movie.ID}.")

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
                user_input: str = input("[1] Ajouter\n[2] Modifier\n[3] Supprimer\n[0] Quitter\n=> ")
                match user_input:
                    case "1":
                        titre = self.show_title()
                        annee_production = self.show_annee_production()
                        genre = self.show_genre()
                        age_limit = self.show_age_limit()
                        manip_data.add_movie(file_path=self.file_path, titre=titre, annee_production=annee_production, genre=genre, age_limite=age_limit)
                        print("Film correctement ajouté !")
                    case "2":
                        id = self.show_id()
                        titre = self.show_title()
                        annee_production = self.show_annee_production()
                        genre = self.show_genre()
                        age_limit = self.show_age_limit()
                        manip_data.mofify_movie(file_path=self.file_path, id=id, titre=titre, annee_production=annee_production, genre=genre, age_limite=age_limit)
                        print("Film correctement modifié !")
                    case "3":
                        id = self.show_id()
                        manip_data.remove_movie(file_path=self.file_path, id=id)
                        print("Film correctement retiré !")
                    case "0":
                        break
                    case _:
                        raise InvalidSignalException("Erreur de saisie. Veuillez recommencer.")
            except InvalidSignalException as e:
                e.display_message_error