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

# Ajouter un film
    # Demander les informations nécessaires à l’utilisateur.
    # Créer un objet Movie.
    # Ajouter ce film dans le fichier movies.csv.
    # Commiter votre travail & merge.

def add_movie(file_path: Path, titre: str, annee_production: int, genre:str, age_limite: int) -> None:
    movies: dict[int, Movie] = load_csv(file_path=file_path)
    movie: Movie = Movie(
        titre=titre,
        annee_production=annee_production,
        genre=genre,
        age_limite=age_limite
    )
    movies.update({Movie.ID: movie})
    write_csv(file_path=file_path, movies=movies)

# Modifier un film
    # Demander l'id du film à modifier.
    # Redemander toutes les informations du film (remplacement complet).
    # Mettre à jour le fichier CSV.
    # Commiter votre travail & merge.

def mofify_movie(file_path: Path, id: int, titre: str, annee_production: int, genre:str, age_limite: int) -> None:
    movies: dict[int, Movie] = load_csv(file_path=file_path)
    if id not in movies.keys():
        raise IndexError(f"'{id}' is not a key of movies")
    movie: Movie = movies[id]
    movie.titre = titre
    movie.annee_production = annee_production
    movie.genre = genre
    movie.age_limite = age_limite
    write_csv(file_path=file_path, movies=movies)

# Supprimer un film
    # Supprimer un film sur la base de son id.
    # Commiter votre travail & merge .
    # Si possible, chaque action doit être développée sur une branche Git dédiée, puis mergée dans la branche principale.

def remove_movie(file_path: Path, id: int) -> None:
    movies: dict[int, Movie] = load_csv(file_path=file_path)
    if id not in movies.keys():
        raise IndexError(f"There is no movie with id : '{id}'.")
    movies.pop(id)
    write_csv(file_path=file_path, movies=movies)
