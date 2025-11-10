from pathlib import Path

from utils.csv_manager import load_csv
from menu_write import MenuWrite


def main() -> None:
    file_path = Path("./data/movies.csv")
    # The database is loaded to assign the Movie.ID class variable.
    load_csv(file_path=file_path)
    menu_read = MenuWrite(file_path=file_path)
    menu_read.show()


if __name__ == "__main__":
    main()
