from pathlib import Path

from models.movies import Movie
from utils.csv_manager import load_csv
from utils.genre import Genre


def get_movies_title(file_path: Path, titre: str) -> list[Movie]:
    if type(titre) is not str:
        raise TypeError("The type of 'titre' must be str.")
    movies: dict[int, Movie] = load_csv(file_path=file_path)
    valid_movies: list[Movie] = []
    for movie in movies.values():
        if titre in movie.titre:
            valid_movies.append(movie)
    return valid_movies


def get_movies_age_limit(file_path: Path, age_limite: int) -> list[Movie]:
    if type(age_limite) is not int:
        raise TypeError("The type of 'age_limite' must be int.")
    if age_limite < 0:
        raise ValueError("'age_limit' must be greater than or equal to 0.")
    movies: dict[int, Movie] = load_csv(file_path=file_path)
    valid_movies: list[Movie] = []
    for movie in movies.values():
        if movie.age_limite <= age_limite:
            valid_movies.append(movie)
    return valid_movies


def get_movies_genre(file_path: Path, genre: Genre) -> list[Movie]:
    if not isinstance(genre, Genre):
        raise TypeError("'genre' must be an instance of the class Genre.")
    movies: dict[int, Movie] = load_csv(file_path=file_path)
    valid_movies: list[Movie] = []
    for movie in movies.values():
        if movie.genre == genre:
            valid_movies.append(movie)
    return valid_movies


def get_movies_annees_production(
    file_path: Path, annee_production1: int, annee_production2: int
) -> list[Movie]:
    if type(annee_production1) is not int:
        raise TypeError("The type of 'annee1' must be str.")
    if type(annee_production2) is not int:
        raise TypeError("The type of 'annee2' must be str.")
    if annee_production1 > annee_production2:
        raise TypeError("'annee1' must be less than or equal to 'annee2'")
    movies: dict[int, Movie] = load_csv(file_path=file_path)
    valid_movies: list[Movie] = []
    for movie in movies.values():
        if annee_production1 <= movie.annee_production <= annee_production2:
            valid_movies.append(movie)
    return valid_movies
