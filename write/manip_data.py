from pathlib import Path
import csv

from models.movies import Movie


class PathDoesNotExistException(Exception):
    def __init__(self, msg: str, *args):
        super().__init__(*args)
        self.msg = msg
    
    def display_message_error(self) -> None:
        print(self.msg)


class ManipData():
    def __init__(self, file_path: Path):
        if not file_path.exists():
            raise PathDoesNotExistException(f"path : '{file_path}' does not exist.")
        self.file_path: Path = file_path
        self.movies: dict[int, Movie] = self.load_csv()

    def load_csv(self) -> dict[int, Movie]:
        movies: dict[Movie] = {}
        with open(file=self.file_path, mode="rt", encoding="utf-8", newline="") as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                movies.update({row['id']: Movie(titre=row['titre'], annee_production=row['annee_production'], genre=row['genre'], age_limite=row['age_limite'])})
        return movies

    def write_csv(self) -> None:
        if not(isinstance(self.movies, dict) and all(isinstance(movie, Movie) for movie in self.movies.values())):
            raise TypeError("'movies' must be a dict whose values are instances of the class Movie.")
        with open(file=self.file_path, mode="wt", encoding="utf-8", newline="") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            for id, movie in self.movies.items():
                csv_writer.writerow([id, movie.titre, movie.annee_production, movie.genre, movie.age_limite])

    # Ajouter un film
        # Demander les informations nécessaires à l’utilisateur.
        # Créer un objet Movie.
        # Ajouter ce film dans le fichier movies.csv.
        # Commiter votre travail & merge.

    def add_movie(self, titre: str, annee_production: int, genre:str, age_limite: int) -> None:
        id_movie = max(list(self.movies.keys())) + 1
        self.movies.update({id_movie: Movie(titre=titre, annee_production=annee_production, genre=genre, age_limite=age_limite)})
        self.write_csv()

    # Modifier un film
        # Demander l'id du film à modifier.
        # Redemander toutes les informations du film (remplacement complet).
        # Mettre à jour le fichier CSV.
        # Commiter votre travail & merge.

    def mofify_movie(self, id: int, titre: str, annee_production: int, genre:str, age_limite: int) -> None:
        movie: Movie = self.movies[id]

    # Supprimer un film
        # Supprimer un film sur la base de son id.
        # Commiter votre travail & merge .
        # Si possible, chaque action doit être développée sur une branche Git dédiée, puis mergée dans la branche principale.