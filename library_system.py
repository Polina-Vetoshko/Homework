from typing import List, Dict, Optional

class BookAlreadyIssuedError(Exception):
    """Книга уже выдана и не может быть выдана повторно."""
    ...

class BookNotIssuedError(Exception):
    """Книга уже доступна и не может быть возвращена."""
    ...

class BookNotFoundError(Exception):
    """Книга с указанным ISBN отсутствует в библиотеке."""
    ...

class Book:
    """Книга: хранит неизменяемые данные и свой статус."""

    def __init__(self, isbn: str, title: str, author: str) -> None:
        # Приватные атрибуты: метаданные фиксируем навсегда
        self.__isbn: str = isbn
        self.__title: str = title
        self.__author: str = author
        self.__is_available: bool = True

    @property
    def isbn(self) -> str:
        return self.__isbn

    @property
    def title(self) -> str:
        return self.__title

    @property
    def author(self) -> str:
        return self.__author

    @property
    def is_available(self) -> bool:
        return self.__is_available

    def issue(self) -> None:
        """Пометить книгу как выданную, если она доступна."""
        if not self.__is_available:
            raise BookAlreadyIssuedError("Книга уже выдана.")
        self.__is_available = False

    def return_book(self) -> None:
        """Пометить книгу как возвращённую, если она была выдана."""
        if self.__is_available:
            raise BookNotIssuedError("Книга не была выдана.")
        self.__is_available = True

   
    def __repr__(self) -> str:
        status = "доступна" if self.__is_available else "выдана"
        return f"Book({self.__title!r}, {self.__isbn!r}, статус={status})"


class Library:
    """Библиотека: управляет коллекцией книг и выдачей/возвратом."""

    def __init__(self) -> None:
        # Связь
        self.__books: Dict[str, Book] = {}

    def add_book(self, book: Book) -> None:
        """Добавить книгу в библиотеку."""
        self.__books[book.isbn] = book

    def get_book(self, isbn: str) -> Optional[Book]:
        """Найти книгу по ISBN."""
        return self.__books.get(isbn)

    def checkout_book(self, isbn: str) -> None:
        """Выдать книгу читателю (через библиотеку)."""
        book = self.__books.get(isbn)
        if book is None:
            raise ValueError("Книга не найдена в библиотеке.")
        book.issue()

    def return_book(self, isbn: str) -> None:
        """Вернуть книгу в библиотеку."""
        book = self.__books.get(isbn)
        if book is None:
            raise ValueError("Книга не найдена в библиотеке.")
        book.return_book()

    def list_all_books(self) -> List[Book]:
        """Список всех книг."""
        return list(self.__books.values())

    def list_available_books(self) -> List[Book]:
        """Только доступные книги."""
        return [b for b in self.__books.values() if b.is_available]

    def list_checked_out_books(self) -> List[Book]:
        """Только выданные книги."""
        return [b for b in self.__books.values() if not b.is_available]



