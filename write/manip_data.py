from pathlib import Path

from models.movies import Movie
from utils.csv_manager import load_csv, write_csv
from utils.genre import Genre


def add_movie(
    file_path: Path, titre: str, annee_production: int, genre: Genre, age_limite: int
) -> None:
    movies: dict[int, Movie] = load_csv(file_path=file_path)
    movie: Movie = Movie(
        titre=titre,
        annee_production=annee_production,
        genre=genre,
        age_limite=age_limite,
    )
    movies.update({Movie.ID: movie})
    write_csv(file_path=file_path, movies=movies)


def mofify_movie(
    file_path: Path,
    id: int,
    titre: str,
    annee_production: int,
    genre: Genre,
    age_limite: int,
) -> None:
    movies: dict[int, Movie] = load_csv(file_path=file_path)
    if id not in movies.keys():
        raise IndexError(f"'{id}' is not a key of movies")
    movie: Movie = movies[id]
    movie.titre = titre
    movie.annee_production = annee_production
    movie.genre = genre
    movie.age_limite = age_limite
    write_csv(file_path=file_path, movies=movies)


def remove_movie(file_path: Path, id: int) -> None:
    movies: dict[int, Movie] = load_csv(file_path=file_path)
    if id not in movies.keys():
        raise IndexError(f"There is no movie with id : '{id}'.")
    movies.pop(id)
    write_csv(file_path=file_path, movies=movies)
