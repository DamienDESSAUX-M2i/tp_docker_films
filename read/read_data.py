from pathlib import Path
import csv

from models.movies import Movie
from read.exceptions.path_does_not_exist_exception import PathDoesNotExistException


def load_csv(file_path: Path) -> dict[int, Movie]:
    if not file_path.exists():
        raise PathDoesNotExistException(f"path : '{file_path}' does not exist.")
    Movie.ID = 0
    movies: dict[Movie] = {}
    with open(file=file_path, mode="rt", encoding="utf-8", newline="") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            movie: Movie = Movie(titre=row['titre'], annee_production=int(row['annee_production']), genre=row['genre'], age_limite=int(row['age_limite']))
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

def get_movies_title(file_path: Path, titre: str) -> list[Movie]:
    if type(titre) is not str:
        raise TypeError("The type of 'titre' must be str.")
    movies: dict[int, Movie] = load_csv(file_path=file_path)
    movies_accepted: list[Movie] = []
    for movie in movies.values():
        if titre in movie.titre:
            movies_accepted.append(movie)
    return movies_accepted

# Récupérer la liste des films ayant une limite d’âge inférieure ou égale à une valeur donnée.

def get_movies_age_limit(file_path: Path, age_limite: int) -> list[Movie]:
    if type(age_limite) is not int:
        raise TypeError("The type of 'age_limite' must be int.")
    movies: dict[int, Movie] = load_csv(file_path=file_path)
    movies_accepted: list[Movie] = []
    for movie in movies.values():
        if movie.age_limite <= age_limite:
            movies_accepted.append(movie)
    return movies_accepted

# Récupérer la liste des films d’un certain genre.

def get_movies_genre(file_path: Path, genre: str) -> list[Movie]:
    if type(genre) is not str:
        raise TypeError("The type of 'genre' must be str.")
    movies: dict[int, Movie] = load_csv(file_path=file_path)
    movies_accepted: list[Movie] = []
    for movie in movies.values():
        if movie.genre == genre:
            movies_accepted.append(movie)
    return movies_accepted

# Récupérer la liste des films produits entre deux années données (année de début et année de fin).

def get_movies_annees_production(file_path: Path, annee_production1: int, annee_production2: int) -> list[Movie]:
    if type(annee_production1) is not int:
        raise TypeError("The type of 'annee1' must be str.")
    if type(annee_production2) is not int:
        raise TypeError("The type of 'annee2' must be str.")
    if annee_production1 > annee_production2:
        raise TypeError("'annee1' must be less than or equal to 'annee2'")
    movies: dict[int, Movie] = load_csv(file_path=file_path)
    movies_accepted: list[Movie] = []
    for movie in movies.values():
        if annee_production1 <= movie.annee_production <= annee_production2:
            movies_accepted.append(movie)
    return movies_accepted