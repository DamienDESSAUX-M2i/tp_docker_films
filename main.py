from pathlib import Path

from write.manip_data import ManipData


def main() -> None:
    file_path = Path("data/movies.csv")
    manip_data = ManipData(file_path=file_path)
    manip_data.add_movie("titre", 2000, "genre", 18)
    manip_data.mofify_movie(1, "titre", 0, "genre", 0)
    manip_data.remove_movie(1)


if __name__ == "__main__":
    main()