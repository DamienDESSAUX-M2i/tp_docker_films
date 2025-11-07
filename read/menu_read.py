from pathlib import Path

from models.movie import Movie
from utils.genre import Genre
from utils.menu import Menu
import read_data
from exceptions.invalid_signal_exception import InvalidSignalException


class MenuRead(Menu):
    def __init__(self, file_path: Path):
        self.file_path = file_path

    def get_movies_with_title(self) -> None:
        print("=== Chercher un film par titre ===")
        titre: str = self.show_title(msg="Titre : ")
        movies: list[Movie] = read_data.get_movies_title(
            file_path=self.file_path, titre=titre
        )
        print(f"=== Liste des films dont le titre contient {titre} ===")
        for movie in movies:
            print(movie)
            print("")

    def get_movies_with_age_limit(self) -> None:
        print("=== Chercher un film par age limite ===")
        age_limit: int = self.show_age_limit(
            msg="Age limite : ",
            msg_error="L'âge doit être un nombre entier positif.",
        )
        movies: list[Movie] = read_data.get_movies_age_limit(
            file_path=self.file_path, age_limite=age_limit
        )
        print(
            f"=== Liste des films dont l'âge limit est supérieur ou égal à {age_limit} ==="
        )
        for movie in movies:
            print(movie)
            print("")

    def get_movies_with_genre(self) -> None:
        print("=== Chercher un film par genre ===")
        genre: Genre = self.show_genre(
            msg="Genre : ",
            msg_error=f"Le genre n'est pas valide.\nLa liste des genres valide est : {', '.join(Genre.get_values())}.",
        )
        movies: list[Movie] = read_data.get_movies_genre(
            file_path=self.file_path, genre=genre
        )
        print(f"=== Liste des films du genre {genre} ===")
        for movie in movies:
            print(movie)
            print("")

    def get_movies_with_year_production(self) -> None:
        print("=== Chercher un film par année de production ===")
        annee_production1: int = self.show_annee_production(
            msg="Année de production (borne inférieure) : ",
            msg_error="L'année de production doit être un nombre entier supérieur ou égal à 0.",
            born_inf=0,
        )
        annee_production2: int = self.show_annee_production(
            msg="Année de production (borne inférieure) : ",
            msg_error="L'année de production doit être un nombre entier supérieur ou égal à 0.",
            born_inf=annee_production1,
        )
        movies: list[Movie] = read_data.get_movies_annees_production(
            file_path=self.file_path,
            annee_production1=annee_production1,
            annee_production2=annee_production2,
        )
        print(
            f"=== Liste des films dont l'année de production est entre {annee_production1} et {annee_production2} ==="
        )
        for movie in movies:
            print(movie)
            print("")

    def show(self):
        while True:
            try:
                user_input: str = input(
                    "[1] Chercher un film par son titre\n[2] Chercher un film par limite d'âge\n[3] Chercher un film par son genre\n[4] Chercher un film par son année de production\n[0] Quitter\n=> "
                )
                match user_input:
                    case "1":
                        self.get_movies_with_title()
                    case "2":
                        self.get_movies_with_age_limit()
                    case "3":
                        self.get_movies_with_genre()
                    case "4":
                        self.get_movies_with_year_production()
                    case "0":
                        break
                    case _:
                        raise InvalidSignalException(
                            "Erreur de saisie. Veuillez recommencer."
                        )
            except InvalidSignalException as e:
                e.display_message_error()
