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
    id_movie: int,
    titre: str,
    annee_production: int,
    genre: Genre,
    age_limite: int,
) -> None:
    movies: dict[int, Movie] = load_csv(file_path=file_path)
    if id_movie not in movies.keys():
        raise IndexError(f"'{id_movie}' is not a key of movies")
    movie: Movie = movies[id_movie]
    movie.titre = titre
    movie.annee_production = annee_production
    movie.genre = genre
    movie.age_limite = age_limite
    write_csv(file_path=file_path, movies=movies)


def remove_movie(file_path: Path, id_movie: int) -> None:
    movies: dict[int, Movie] = load_csv(file_path=file_path)
    if id_movie not in movies.keys():
        raise IndexError(f"There is no movie with id_movie : '{id_movie}'.")
    movies.pop(id_movie)
    write_csv(file_path=file_path, movies=movies)
