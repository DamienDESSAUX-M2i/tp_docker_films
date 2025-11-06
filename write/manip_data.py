from pathlib import Path
import csv

from models.movies import Movie

# Ajouter un film
    # Demander les informations nécessaires à l’utilisateur.
    # Créer un objet Movie.
    # Ajouter ce film dans le fichier movies.csv.
    # Commiter votre travail & merge.

# Modifier un film
    # Demander l'id du film à modifier.
    # Redemander toutes les informations du film (remplacement complet).
    # Mettre à jour le fichier CSV.
    # Commiter votre travail & merge.

# Supprimer un film
    # Supprimer un film sur la base de son id.
    # Commiter votre travail & merge .
    # Si possible, chaque action doit être développée sur une branche Git dédiée, puis mergée dans la branche principale.

class PathException(Exception):
    def __init__(self, msg: str, *args):
        super().__init__(*args)
        self.msg = msg
    
    def display_message_error(self) -> None:
        print(self.msg)


def load_csv(file_path: Path) -> dict[int, Movie]:
    if not Path.exists(file_path):
        raise PathException(f"path : '{file_path}' does not exist.")
    movies: dict[Movie] = {}
    with open(file=file_path, mode="rt", encoding="utf-8", newline="") as csv_file:
        csv_reader = csv.reader(csvfile=csv_file, delimiter=',')
        for row in csv_reader:
            movies.update({row['id']: Movie(titre=row['titre'])})
    return movies


def write_csv(file_path: Path, movies: dict[int, Movie]) -> None:
    if not Path.exists(file_path):
        raise PathException(f"path : '{file_path}' does not exist.")
    if not(isinstance(movies, dict) and all(isinstance(movie, Movie) for movie in movies.values())):
        raise TypeError("'movies' must be a dict whose values are instances of the class Movie.")
    with open(file=file_path, mode="wt", encoding="utf-8", newline="") as csv_file:
        csv_writer = csv.writer(csvfile=csv_file, delimiter=',')
        for id, movie in movies.items():
            csv_writer.writerow([id, movie.titre, movie.annee_production, movie.genre, movie.age_limite])