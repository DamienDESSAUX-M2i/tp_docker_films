from pathlib import Path

from write.manip_data import ManipData


def main() -> None:
    file_path = Path("data/movies.csv")
    manip_data = ManipData(file_path=file_path)
    print(manip_data.movies)
    manip_data.add_movie("titre", 2000, "genre", 18)
    print(manip_data.movies)


if __name__ == "__main__":
    main()