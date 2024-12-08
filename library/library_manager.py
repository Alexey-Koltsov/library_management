from models import Library


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

if __name__ == "__main__":
    main()
