"""
Консольное приложение для управления библиотекой книг.
Приложение позволяет добавлять, удалять, искать и отображать книги.
Каждая книга содержит следующие поля:
• id (уникальный идентификатор, генерируется автоматически)
• title (название книги)
• author (автор книги)
• year (год издания)
• status (статус книги: “в наличии”, “выдана”)
"""


import json


class Book:
    """Класс книги"""

    def __init__(self,
                 id: int,
                 title: str,
                 author: str,
                 year: int,
                 status: str = 'в наличии',
                 ) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self):
        return f'ID: {self.id}, ' \
               f'Название: {self.title}, ' \
               f'Автор: {self.author}, ' \
               f'Год издания: {self.year}, ' \
               f'Статус: {self.status}'


class Library:
    """Класс библиотека"""

    def __init__(self,
                 filename: str = 'library.json',
                 ) -> None:
        self.filename = filename
        self.books = self.load_books()

    def load_books(self) -> list[Book]:
        """Загрузка данных из файла"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                books = []
                for book in json.load(file):
                    book = Book(**book)
                    books.append(book)
            return books
        except FileNotFoundError:
            print('Файл не найден')

    def set_book_id(self) -> int:
        """Получение id для сохраняемой книги"""
        try:
            books = self.load_books()
            book_id: int = max([book.id for book in books], default=0) + 1
            return book_id
        except ValueError:
            return 'Ошибка получения id для сохраняемой книги'

    def save_books_to_file(self) -> None:
        """Сохранение книг в файл"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump([book.__dict__ for book in self.books],
                          file, ensure_ascii=False, indent=4)
        except FileNotFoundError:
            print('Файл не найден')

    def add_book(self, title: str, author: str, year: int) -> list[Book]:
        """Добавление книги"""
        try:
            id: int = self.set_book_id()
            book: Book = Book(id, title, author, year)
            self.books.append(book)
            self.save_books_to_file()
            book: Book = self.books[-1]
            return book
        except ValueError:
            return 'Ошибка добавления книги'

    def delete_book(self, id: int) -> str:
        """Удаление книги"""
        try:
            for book in self.books:
                if book.id == id:
                    self.books.remove(book)
                    self.save_books_to_file()
                    return 'Книга удалена'
            return 'Книга с таким ID не найдена'
        except ValueError:
            return 'Ошибка удаления книги'

    def search_book(self, query, field) -> list[Book]:
        """Поиск книги по (title/author/year)"""
        try:
            results: list[Book] = []
            for book in self.books:
                if query.lower() in str(getattr(book, field)).lower():
                    results.append(book)
            return results
        except ValueError:
            return 'Ошибка поиска книги'

    def change_status(self, id: int, status: str) -> str:
        """Изменение статуса книги"""
        try:
            change_status: dict = {
                'в наличии': 'выдана',
                'выдана': 'в наличии'
            }
            for book in self.books:
                if book.id == id:
                    if status == book.status:
                        return 'Статус книги не изменен'
                    elif status not in change_status.keys():
                        return 'Данного статуса не существует'
                    book.status = change_status[book.status]
                    print(book)
                    self.save_books_to_file()
                    return 'Статус книги обновлен'
            return 'Книга с таким id не найдена'
        except ValueError:
            return 'Ошибка изменения статуса книги'

    def __str__(self):
        for book in self.books:
            result: str = ''
            result += f'ID: {book.id}, ' \
                      f'Название: {book.title}, ' \
                      f'Автор: {book.author}, ' \
                      f'Год издания: {book.year}, ' \
                      f'Статус: {book.status} '
        return result
