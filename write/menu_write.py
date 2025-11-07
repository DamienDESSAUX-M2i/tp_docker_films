from pathlib import Path

from models.movies import Movie
from utils.genre import Genre
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
        user_input: str = input("Id : ")
        if user_input.isdigit():
            user_input = int(user_input)
            if 1 <= user_input <= Movie.ID:
                return user_input
        raise InvalidTitleException(
            f"L'identifiant doit être un nombre entier compris entre 1 et {Movie.ID}."
        )

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
                    "[1] Ajouter\n[2] Modifier\n[3] Supprimer\n[0] Quitter\n=> "
                )
                match user_input:
                    case "1":
                        titre = self.show_title()
                        annee_production = self.show_annee_production(
                            "Année de production : "
                        )
                        genre = self.show_genre()
                        age_limit = self.show_age_limit()
                        manip_data.add_movie(
                            file_path=self.file_path,
                            titre=titre,
                            annee_production=annee_production,
                            genre=genre,
                            age_limite=age_limit,
                        )
                        print("Film correctement ajouté !")
                    case "2":
                        id = self.show_id()
                        titre = self.show_title()
                        annee_production = self.show_annee_production(
                            "Année de production : "
                        )
                        genre = self.show_genre()
                        age_limit = self.show_age_limit()
                        manip_data.mofify_movie(
                            file_path=self.file_path,
                            id=id,
                            titre=titre,
                            annee_production=annee_production,
                            genre=genre,
                            age_limite=age_limit,
                        )
                        print("Film correctement modifié !")
                    case "3":
                        id = self.show_id()
                        manip_data.remove_movie(file_path=self.file_path, id=id)
                        print("Film correctement retiré !")
                    case "0":
                        break
                    case _:
                        raise InvalidSignalException(
                            "Erreur de saisie. Veuillez recommencer."
                        )
            except InvalidSignalException as e:
                e.display_message_error
