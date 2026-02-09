books = [
    {'genre': 'поэзия', 'number': '978-5-1000-1234-7', 'title': 'Евгений Онегин', 'author': 'Александр Пушкин'},
    {'genre': 'фэнтези', 'number': '88006', 'title': 'Властелин колец', 'author': 'Джон Р. Р. Толкин'},
    {'genre': 'детектив', 'number': 'D-1122', 'title': 'Безмолвный свидетель', 'author': 'Агата Кристи'}
]

directories = {
    '1': ['978-5-1000-1234-7', '88006'],
    '2': ['D-1122'],
    '3': []
}

def find_book_by_number(number) -> list:
    title = ''
    author = ''

    for book in books:
        if book['number'] == number:
            title = book['title']
            author = book['author']
            break

    return [title, author]

def print_book_title_and_author(number):
    title, author = find_book_by_number(number)

    if title != '' and author != '':
        print(f'Название книги: {title}\nАвтор: {author}')
    else:
        print('Книга не найдена в базе.')

def find_book_position(book_name):
    directory = ''

    for book in books:
        if book['title'] == book_name:
            for key, book_number_list in directories.items():
                if book['number'] in book_number_list:
                    directory = key
                    break
    return directory

def print_book_position(book_name):
    directory = find_book_position(book_name)
    if directory != '':
        print(f'Книга хранится на полке: {directory}')
    else:
        print('Книга не найдена в базе.')

def get_info_about_all_books():
    for book in books:
        print(f'№: {book['number']}, жанр: {book['genre']}, название: {book['title']}, автор: {book['author']}, полка хранения: {find_book_position(book['title'])}')

def add_shelf(shelf_number):
    keys = directories.keys()
    if shelf_number not in keys:
        directories.setdefault(shelf_number, [])
        return f'Полка добавлена. Текущий перечень полок: {", ".join(sorted(directories.keys()))}'
    else:
        return f'Такая полка уже существует. Текущий перечень полок: {", ".join(sorted(keys))}'

def del_shelf(shelf_number):
    shelf = directories.get(shelf_number)
    if shelf is not None and shelf == []:
        directories.pop(shelf_number)
        print(f'Полка удалена. Текущий перечень полок: {", ".join(sorted(directories.keys()))}.')
    elif shelf is not None and shelf != []:
        print(f'На полке есть книги, удалите их перед удалением полки. Текущий перечень полок: {", ".join(sorted(directories.keys()))}.')
    else:
        print(f'Такой полки не существует. Текущий перечень полок: {", ".join(sorted(directories.keys()))}.')

def main():
    while True:
        input_data = input('Введите команду: ')
        match input_data:
            case 'book_info':
                print_book_title_and_author(input('Введите номер книги: '))
            case 'shelf':
                print_book_position(input('Введите название книги: '))
            case 'all':
                get_info_about_all_books()
            case 'add_shelf':
                add_shelf(input('Введите номер полки: '))
            case 'del_shelf':
                del_shelf(input('Введите номер полки: '))
            case 'q':
                break
            case _:
                print("Неизвестная команда. Доступные команды: book_info, shelf, all, add_shelf, del_shelf, q")

if __name__ == "__main__":
    main()