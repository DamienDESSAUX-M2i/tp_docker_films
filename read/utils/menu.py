from abc import ABC, abstractmethod
from pathlib import Path

from utils.genre import Genre
from exceptions.path_does_not_exist_exception import PathDoesNotExistException
from exceptions.invalid_id_exception import InvalidIdException
from exceptions.invalid_title_exception import InvalidTitleException
from exceptions.invalid_age_limit_exception import InvalidAgeLimitException
from exceptions.invalid_genre_exception import InvalidGenreException
from exceptions.invalid_year_exception import InvalidYearException


class Menu(ABC):
    def __init__(self, file_path: Path):
        self._file_path: Path = None
        self.file_path = file_path

    @property
    def file_path(self) -> Path:
        return self._file_path

    @file_path.setter
    def file_path(self, file_path: Path) -> None:
        if not file_path.exists():
            raise PathDoesNotExistException(f"path : '{file_path}' does not exist.")
        self._file_path = file_path

    def user_input_id(
        self, born_inf: int, born_sup: int, msg: str, msg_error: str
    ) -> str:
        if type(born_inf) is not int:
            raise TypeError("The type of 'born_inf' must be int.")
        if type(born_sup) is not int:
            raise TypeError("The type of 'born_sup' must be int.")
        if born_inf > born_sup:
            raise ValueError("'born_inf must be les than or equal to 'born_sup'.")
        user_input: str = input(msg)
        if user_input.isdigit():
            user_input: int = int(user_input)
            if born_inf <= user_input <= born_sup:
                return user_input
        raise InvalidTitleException(msg_error)

    def user_input_title(self, msg: str) -> str:
        return input(msg).title()

    def user_input_annee_production(
        self, born_inf: int, msg: str, msg_error: str
    ) -> int:
        if type(born_inf) is not int:
            raise TypeError(msg)
        user_input: str = input(msg)
        if user_input.isdigit():
            user_input: int = int(user_input)
            if user_input >= born_inf:
                return user_input
        raise InvalidAgeLimitException(msg_error)

    def user_input_genre(self, msg: str, msg_error: str) -> str:
        user_input: str = input(msg).title()
        if user_input in Genre.get_values():
            return Genre(user_input)
        raise InvalidGenreException(msg_error)

    def user_input_age_limit(self, msg: str, msg_error: str) -> int:
        user_input: str = input(msg)
        if user_input.isdigit():
            user_input: int = int(user_input)
            if user_input >= 0:
                return user_input
        raise InvalidYearException(msg_error)

    def show_id(self, born_inf: int, born_sup: int, msg: str, msg_error: str) -> int:
        while True:
            try:
                id_movie = self.user_input_id(
                    born_inf=born_inf, born_sup=born_sup, msg=msg, msg_error=msg_error
                )
                return id_movie
            except InvalidIdException as e:
                e.display_message_error()

    def show_title(self, msg: str) -> str:
        while True:
            try:
                titre = self.user_input_title(msg=msg)
                return titre
            except InvalidTitleException as e:
                e.display_message_error()

    def show_annee_production(self, born_inf: int, msg: str, msg_error: str) -> int:
        while True:
            try:
                annee_production = self.user_input_annee_production(
                    born_inf=born_inf, msg=msg, msg_error=msg_error
                )
                return annee_production
            except InvalidAgeLimitException as e:
                e.display_message_error()

    def show_genre(self, msg: str, msg_error: str) -> str:
        while True:
            try:
                genre = self.user_input_genre(msg=msg, msg_error=msg_error)
                return genre
            except InvalidGenreException as e:
                e.display_message_error()

    def show_age_limit(self, msg: str, msg_error: str) -> int:
        while True:
            try:
                age_limit = self.user_input_age_limit(msg=msg, msg_error=msg_error)
                return age_limit
            except InvalidYearException as e:
                e.display_message_error()

    @abstractmethod
    def show(self) -> None:
        raise NotImplementedError
