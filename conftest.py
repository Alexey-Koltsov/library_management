import pytest

from library.models import Library


@pytest.fixture(autouse=True)
def create_and_clear_test_library():
    """
    Создание и очиствка тестового файла
    для сохранения книг
    """
    file = open("test_library.json", "w+")
    file.write("{}")
    file.close()
    yield
    file = open("test_library.json", "w+")
    file.write("{}")
    file.close()


@pytest.fixture(autouse=True)
def library():
    return Library('test_library.json')


@pytest.fixture(autouse=True)
def library_add_book(library):
    return library.add_book
