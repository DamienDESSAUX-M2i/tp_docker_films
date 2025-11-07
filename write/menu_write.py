from pathlib import Path

from models.movie import Movie
from utils.genre import Genre
from utils.menu import Menu
import manip_data
from exceptions.invalid_signal_exception import InvalidSignalException


class MenuWrite(Menu):
    def __init__(self, file_path: Path):
        Menu.__init__(self, file_path=file_path)

    def add_movie(self) -> None:
        print("=== Ajouter un film ===")
        titre: str = self.show_title(msg="Titre : ")
        annee_production: int = self.show_annee_production(
            msg="Année de production : ",
            msg_error="L'année de production doit être un nombre entier supérieur ou égal à 0.",
            born_inf=0,
        )
        genre: Genre = self.show_genre(
            msg="Genre : ",
            msg_error=f"Le genre n'est pas valide.\nLa liste des genres valide est : {', '.join(Genre.get_values())}.",
        )
        age_limit: int = self.show_age_limit(
            msg="Age limite : ",
            msg_error="L'âge doit être un nombre entier positif.",
        )
        manip_data.add_movie(
            file_path=self.file_path,
            titre=titre,
            annee_production=annee_production,
            genre=genre,
            age_limite=age_limit,
        )
        print("Film correctement ajouté !")

    def modify_movie(self) -> None:
        print("=== Modifier un film ===")
        id_movie = self.show_id(
            born_inf=1,
            born_sup=Movie.ID,
            msg="ID : ",
            msg_error=f"L'identifiant doit être un nombre entier compris entre 1 et {Movie.ID}.",
        )
        titre: str = self.show_title(msg="Titre : ")
        annee_production: int = self.show_annee_production(
            msg="Année de production : ",
            msg_error="L'année de production doit être un nombre entier supérieur ou égal à 0.",
            born_inf=0,
        )
        genre: Genre = self.show_genre(
            msg="Genre : ",
            msg_error=f"Le genre n'est pas valide.\nLa liste des genres valide est : {', '.join(Genre.get_values())}.",
        )
        age_limit: int = self.show_age_limit(
            msg="Age limite : ",
            msg_error="L'âge doit être un nombre entier positif.",
        )
        manip_data.mofify_movie(
            file_path=self.file_path,
            id_movie=id_movie,
            titre=titre,
            annee_production=annee_production,
            genre=genre,
            age_limite=age_limit,
        )
        print("Film correctement modifié !")

    def remove_movie(self) -> None:
        print("=== Supprimer un film ===")
        id_movie: int = self.show_id(
            born_inf=1,
            born_sup=Movie.ID,
            msg="ID : ",
            msg_error=f"L'identifiant doit être un nombre entier compris entre 1 et {Movie.ID}.",
        )
        manip_data.remove_movie(file_path=self.file_path, id_movie=id_movie)
        print("Film correctement supprimé !")

    def show(self):
        while True:
            try:
                user_input: str = input(
                    "[1] Ajouter\n[2] Modifier\n[3] Supprimer\n[0] Quitter\n=> "
                )
                match user_input:
                    case "1":
                        self.add_movie()
                    case "2":
                        self.modify_movie()
                    case "3":
                        self.remove_movie()
                    case "0":
                        break
                    case _:
                        raise InvalidSignalException(
                            "Erreur de saisie. Veuillez recommencer."
                        )
            except InvalidSignalException as e:
                e.display_message_error
