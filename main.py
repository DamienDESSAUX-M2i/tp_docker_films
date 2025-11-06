from pathlib import Path

from ui.menu_write import MenuWrite
from ui.menu_read import MenuRead


def main() -> None:
    file_path = Path("data/movies.csv")
    menu_main = MenuWrite(file_path=file_path)
    menu_read = MenuRead(file_path=file_path)
    menu_main.show()


if __name__ == "__main__":
    main()