class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        """
        Инициализация экземпляра класса Book.

        Args:
            name (str): Название книги.
            author (str): Автор книги.
        """
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """Возвращает название книги."""
        return self._name

    @property
    def author(self) -> str:
        """Возвращает автора книги."""
        return self._author

    def __str__(self) -> str:
        """Возвращает строковое представление книги."""
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        """Возвращает строковое представление книги для отладки."""
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Класс, представляющий бумажную книгу."""

    def __init__(self, name: str, author: str, pages: int):
        """
        Инициализация экземпляра класса PaperBook.

        Args:
            name (str): Название книги.
            author (str): Автор книги.
            pages (int): Количество страниц.
        """
        super().__init__(name, author)
        self.pages = pages  # Используем setter для проверки

    @property
    def pages(self) -> int:
        """Возвращает количество страниц."""
        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:
        """
        Устанавливает количество страниц.

        Args:
            value (int): Количество страниц.

        Raises:
            ValueError: Если количество страниц меньше или равно 0.
        """
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом.")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")
        self._pages = value

    def __str__(self) -> str:
        """Возвращает строковое представление бумажной книги."""
        return f"Бумажная книга {self.name}. Автор {self.author}. Страниц: {self.pages}"


class AudioBook(Book):
    """Класс, представляющий аудиокнигу."""

    def __init__(self, name: str, author: str, duration: float):
        """
        Инициализация экземпляра класса AudioBook.

        Args:
            name (str): Название книги.
            author (str): Автор книги.
            duration (float): Продолжительность аудиокниги.
        """
        super().__init__(name, author)
        self.duration = duration  # Используем setter для проверки

    @property
    def duration(self) -> float:
        """Возвращает продолжительность аудиокниги."""
        return self._duration

    @duration.setter
    def duration(self, value: float) -> None:
        """
        Устанавливает продолжительность аудиокниги.

        Args:
            value (float): Продолжительность аудиокниги.

        Raises:
            ValueError: Если продолжительность меньше или равна 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом.")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = float(value)

    def __str__(self) -> str:
        """Возвращает строковое представление аудиокниги."""
        return f"Аудиокнига {self.name}. Автор {self.author}. Продолжительность: {self.duration} ч."
