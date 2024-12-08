import pytest

from models import Book


@pytest.mark.parametrize(
    'title, author, year',
    [('Приключение Тома Соера', 'Марк Твен', 1876),]
)
def test_add_books(library, title, author, year):
    """Тест на добавление книги"""
    len_before = len(library.books)
    book: Book = library.add_book(title, author, year)
    len_after: int = len(library.books)
    assert book.id == 1
    assert book.title == title
    assert book.author == author
    assert book.year == year
    assert book.status == 'в наличии'
    assert (len_before + 1) == len_after


@pytest.mark.parametrize(
    'title, author, year',
    [('Приключение Тома Соера', 'Марк Твен', 1876),]
)
def test_delete_books(library, title, author, year):
    """Тест на удаление книги"""
    book: Book = library.add_book(title, author, year)
    len_before: int = len(library.books)
    message: str = library.delete_book(book.id)
    len_after: int = len(library.books)
    assert len_before == (len_after + 1)
    assert message == 'Книга удалена'


@pytest.mark.parametrize(
    'title, author, year, field, query',
    [('Женщина в белом', 'Уилки Коллинз', 1860, 'title', 'Женщина в белом'),
     ('Шерлок Холмс', 'Артур Конан Дойл', 1892, 'author', 'Артур Конан Дойл'),
     ('Приключение Тома Соера', 'Марк Твен', 1876, 'year', 1876),
     ]
)
def test_search_book(library, title, author, year, field, query):
    """Тест на поиск книги по (title/author/year)"""
    library.add_book(title, author, year)
    books: list[Book] = library.search_book(query, field)
    assert len(books) == 1
    assert getattr(books[0], field) == query


@pytest.mark.parametrize(
    'data',
    [(('Женщина в белом', 'Уилки Коллинз', 1860),
     ('Шерлок Холмс', 'Артур Конан Дойл', 1892),
     ('Приключение Тома Соера', 'Марк Твен', 1876)),
     ]
)
def test_load_books(library, data):
    """Тест на поиск книги по (title/author/year)"""
    library.add_book(*data[0])
    library.add_book(*data[1])
    library.add_book(*data[2])
    books: list[Book] = library.load_books()
    assert len(books) == 3


@pytest.mark.parametrize(
    'title, author, year, status',
    [('Приключение Тома Соера', 'Марк Твен', 1876, 'выдана'),]
)
def test_change_status(library, title, author, year, status):
    """Тест на изменение статуса книги"""
    book_before: Book = library.add_book(title, author, year)
    book_before_status: str = book_before.status
    library.change_status(book_before.id, status)
    book_after: Book = library.load_books()[0]
    assert book_before_status == 'в наличии'
    assert book_after.status == status
