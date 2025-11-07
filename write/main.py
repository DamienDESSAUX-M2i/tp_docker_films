from pathlib import Path

from menu_write import MenuWrite


def main() -> None:
    file_path = Path("write/data/movies.csv")
    menu_main = MenuWrite(file_path=file_path)
    menu_main.show()


if __name__ == "__main__":
    main()
