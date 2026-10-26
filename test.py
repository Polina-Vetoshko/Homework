from library_system import Library, Book, BookAlreadyIssuedError, BookNotIssuedError, BookNotFoundError

def main():
    lib = Library()

    b1 = Book("978-5-17-113589-6", "Мастер и Маргарита", "Михаил Булгаков")
    b2 = Book("978-2-07-061124-6", "Маленький принц", "Антуан де Сент‑Экзюпери")

    lib.add_book(b1)
    lib.add_book(b2)

    print("Все книги:", lib.list_all_books())
    print("Доступные:", lib.list_available_books())
    print("Выданные:", lib.list_checked_out_books())

    # Выдача
    lib.checkout_book(b1.isbn)
    print("Доступные:", lib.list_available_books())
    print("Выданные:", lib.list_checked_out_books())

    # Повторная выдача 
    try:
        lib.checkout_book(b1.isbn)
    except BookAlreadyIssuedError as e:
        print(e)

    # Возврат
    lib.return_book(b1.isbn)
    print("Доступные:", lib.list_available_books())
    print("Выданные:", lib.list_checked_out_books())

    # Повторный возврат 
    try:
        lib.return_book(b1.isbn)
    except BookNotIssuedError as e:
        print(e)

    # Несуществующий ISBN 
    try:
        lib.checkout_book("000-000-0000")
    except BookNotFoundError as e:
        print(e)

if __name__ == "__main__":
    main()

