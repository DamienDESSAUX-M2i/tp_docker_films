from pathlib import Path

from menu_read import MenuRead


def main() -> None:
    file_path = Path("./data/movies.csv")
    menu_read = MenuRead(file_path=file_path)
    menu_read.show()


if __name__ == "__main__":
    main()