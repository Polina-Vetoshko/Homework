@startuml
class Book {
  -isbn: string
  -author: string
  -title: string
  -isAvailable: boolean
  +getIsbn(): string
  +getAuthor(): string
  +getTitle(): string
  +isAvailable(): boolean
  -setUnavailable(): void
  -setAvailable(): void
}

class Reader {
  -id: string | number
  -name: string
  -borrowedBooks: list<string>
  +getId(): string | number
  +getName(): string
  +borrowBook(isbn: string): boolean
  +returnBook(isbn: string): boolean
}

class Library {
  -books: map<string, Book>
  -issuedBooks: set<string>
  +addBook(isbn: string, author: string, title: string): void
  +lendBook(isbn: string, readerId: string | number): boolean
  +returnBook(isbn: string): boolean
  +getAllBooks(): list<Book>
  +getAvailableBooks(): list<Book>
}

Book "1" -- "*" Library : хранится в
Reader "1" -- "*" Library : обслуживается в
@enduml



**Вопрос 1.** Неизменяемыми должны быть isbn, author и title. ISBN — уникальный идентификатор, его нельзя менять, иначе потеряется связь с учётом. Автор и название описывают саму книгу и после добавления в фонд меняться не должны. Меняется только состояние доступности через специальные методы.

**Вопрос 2.** Состояние «выдана / доступна» лучше хранить в Book, потому что это характеристика самой книги. Но менять его должен только Library, чтобы нельзя было выдать уже выданную книгу или вернуть невыданную. 

**Вопрос 3.** Публичными должны быть методы, образующие API библиотеки: addBook, lendBook, returnBook, getAllBooks, getAvailableBooks. Внутренними должны быть вспомогательные методы: поиск книги по ISBN, проверка читателя, синхронизация флага доступности. Пример метода, который не должен быть публичным, - markIssued(isbn) или removeFromIssuedBooks(isbn): если сделать его публичным, клиент сможет обойти проверки и пометить книгу выданной без читателя или без записи в borrowedBooks. Это нарушит инварианты: книга будет недоступна, но не числиться выданной, или наоборот.