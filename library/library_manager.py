from models import Book, Library


def main():
    library = Library('library.json')

    while True:
        print('\nСистема управления библиотекой')
        print('1 - Добавить книгу')
        print('2 - Удалить книгу')
        print('3 - Искать книги')
        print('4 - Показать все книги')
        print('5 - Изменить статус книги')
        print('6 - Выйти')

        choice = input('Введите номер операции: ')

        if choice == '1':
            title = input('Введите название книги: ')
            author = input('Введите автора книги: ')
            year = int(input('Введите год издания книги: '))
            book: Book = library.add_book(title, author, year)
            print(f'Книга добавлена: {book}')

        elif choice == '2':
            id: int = int(input('Введите ID книги для удаления: '))
            message: str = library.delete_book(id)
            print(message)

        elif choice == '3':
            field: str = input('Искать по полю title/author/year: ')
            query: str = input('Введите значение для поиска: ')
            books: list[Book] = library.search_book(query, field)
            if books:
                for book in books:
                    print(book)
            else:
                print('Книг не найдено')

        elif choice == '4':
            books: list[Book] = library.load_books()
            for book in books:
                print(book)

        elif choice == '5':
            id: int = int(input('Введите ID книги: '))
            status: str = input('Введите статус книги: ')
            message: str = library.change_status(id, status)
            print(message)

        elif choice == '6':
            print('Выход из программы.')
            break

        else:
            print('Неверный выбор. Попробуйте снова.')


if __name__ == "__main__":
    main()
