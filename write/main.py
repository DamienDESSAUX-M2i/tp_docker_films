from pathlib import Path

from models.movie import Movie
from utils.csv_manager import load_csv
from exceptions.empty_data_base_exception import EmptyDataBaseException
from menu_write import MenuWrite


def main() -> None:
    file_path = Path("./data/movies.csv")
    try:
        # The database is loaded to assign the Movie.ID class variable.
        load_csv(file_path=file_path)
        if Movie.ID == 0:
            raise EmptyDataBaseException("La base de donnée est vide.")
        menu_read = MenuWrite(file_path=file_path)
        menu_read.show()
    except EmptyDataBaseException as e:
        e.display_message_error()


if __name__ == "__main__":
    main()
