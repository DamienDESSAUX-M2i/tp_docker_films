from pathlib import Path
import csv

from models.movies import Movie
from exceptions.path_does_not_exist_exception import PathDoesNotExistException


def load_csv(file_path: Path) -> dict[int, Movie]:
    if not file_path.exists():
        raise PathDoesNotExistException(f"path : '{file_path}' does not exist.")
    Movie.ID = 0
    movies: dict[Movie] = {}
    with open(file=file_path, mode="rt", encoding="utf-8", newline="") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            movie: Movie = Movie(titre=row['titre'], annee_production=row['annee_production'], genre=row['genre'], age_limite=row['age_limite'])
            movies.update({Movie.ID: movie})
    return movies

def write_csv(file_path: Path, movies: dict[int, Movie]) -> None:
    if not file_path.exists():
        raise PathDoesNotExistException(f"path : '{file_path}' does not exist.")
    if not(isinstance(movies, dict) and all(isinstance(movie, Movie) for movie in movies.values())):
        raise TypeError("Type of 'movies' must be dict whose values must be instances of class Movie.")
    with open(file=file_path, mode="wt", encoding="utf-8", newline="") as csv_file:
        fieldnames: list[str] = ["id", "titre", "annee_production", "genre", "age_limite"]
        csv_writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=fieldnames)
        csv_writer.writeheader()
        for id, movie in enumerate(movies.values(), start=1):
            csv_writer.writerow({
                "id": id,
                "titre": movie.titre,
                "annee_production": movie.annee_production, 
                "genre": movie.genre,
                "age_limite": movie.age_limite
            })

# Récupérer un film par son titre.

def get_movie_title(file_path: Path, title: str):
    pass

# Commiter votre travail & merge.
# Récupérer la liste des films ayant une limite d’âge inférieure ou égale à une valeur donnée.
# Commiter votre travail & merge.
# Récupérer la liste des films d’un certain genre.
# Commiter votre travail & merge.
# Récupérer la liste des films produits entre deux années données (année de début et année de fin).
# Commiter votre travail & merge.