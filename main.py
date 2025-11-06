from pathlib import Path

from ui.menu_main import MenuMain


def main() -> None:
    file_path = Path("data/movies.csv")
    menu_main = MenuMain(file_path=file_path)
    menu_main.show()


if __name__ == "__main__":
    main()