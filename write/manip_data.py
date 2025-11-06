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
                movie: Movie = Movie(titre=row['titre'], annee_production=row['annee_production'], genre=row['genre'], age_limite=row['age_limite'])
                movies.update({Movie.ID: movie})
        return movies

    def write_csv(self) -> None:
        with open(file=self.file_path, mode="wt", encoding="utf-8", newline="") as csv_file:
            fieldnames: list[str] = ["id", "titre", "annee_production", "genre", "age_limite"]
            csv_writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=fieldnames)
            csv_writer.writeheader()
            for id, movie in self.movies.items():
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

    def add_movie(self, titre: str, annee_production: int, genre:str, age_limite: int) -> None:
        movie: Movie = Movie(titre=titre, annee_production=annee_production, genre=genre, age_limite=age_limite)
        self.movies.update({Movie.ID: movie})
        self.write_csv()

    # Modifier un film
        # Demander l'id du film à modifier.
        # Redemander toutes les informations du film (remplacement complet).
        # Mettre à jour le fichier CSV.
        # Commiter votre travail & merge.

    def mofify_movie(self, id: int, titre: str, annee_production: int, genre:str, age_limite: int) -> None:
        if id not in self.movies.keys():
            raise IndexError(f"'{id}' is not a key of movies")
        movie: Movie = self.movies[id]
        movie.titre = titre
        movie.annee_production = annee_production
        movie.genre = genre
        movie.age_limite = age_limite
        self.write_csv()

    # Supprimer un film
        # Supprimer un film sur la base de son id.
        # Commiter votre travail & merge .
        # Si possible, chaque action doit être développée sur une branche Git dédiée, puis mergée dans la branche principale.
    
    