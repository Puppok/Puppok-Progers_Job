# Классы 

#^ Стандартный способ
name = 'Bobik'
age = 8
isHungry = True
isAlive = True

def bark():
    print(f'{name} says woof woof')

def sleep():
    print(f'{name} 😴...')

def feed(food):
    if isHungry:
        print(f'{name} is eating {food}')
    else:
        print(f'{name} is not hungry')

#^ С помощью класса
# class Имя:
#   общедоступные свойства
#   конструктор класса
#   индивидуальные свойства
#   методы класса

class Dog:
    # общедоступные свойства (одинаковые значения для всех объектов класса)
    paws = 4
    tail = 1
    ears = 2

    # конструктор класса (ф-ция по которой создается объект класса)
    def __init__(self, name: str, age: int, isHungry: bool, breed: str):
        #  индивидуальные свойства (могут отличаться у каждого объекта класса)
        self.name = name
        self.age = age
        self.isHungry = isHungry
        self.breed = breed

    # методы класса
    def bark(self):
        print(f'{self.name} says woof woof')

    def sleep(self):
        print(f'{self.name} 😴...')

    def feed(self, food):
        if self.isHungry:
            print(f'{self.name} is eating {food}')
        else:
            print(f'{self.name} is not hungry')

bobik = Dog('Bobik', 5, True, 'Mops')
bobik.bark()
bobik.feed('meat')
print(f'Имя: {bobik.name}')
print(f'Кол-во лап: {bobik.paws}')
bobik.paws = 10
print(f'Кол-во лап: {bobik.paws}')


# print('--------------')

pushok = Dog('Pushok', 6, False, 'Taksa')
pushok.bark()
pushok.feed('fish')
print(f'Имя: {pushok.name}')
print(f'Кол-во лап: {pushok.paws}')



#^ Задача 1: Класс "Книга" 📚
# Условие:

#~ Создайте класс Book с атрибутами:
# title (название)
# author (автор)
# pages (количество страниц)
# current_page (текущая страница, изначально 0)

#~ Добавьте методы:
# read(pages_count) — читает указанное количество страниц (увеличивает current_page)
# info() — выводит информацию о книге
# is_finished() — возвращает True, если книга дочитана

class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages
        self.currentPage: int = 0
        print('Создан объект класса')

    def read(self, pagesCount: int):
        '''читает указанное количество страниц'''
        self.currentPage += pagesCount
        print(f'Прочитано страниц: {pagesCount}')

    def info(self):
        '''выводит информацию о книге'''
        print(f'Книга: {self.title}, автор: {self.author}, кол-во стр: {self.pages}')

    def isFinished(self):
        '''проверяет, прочитана ли книга'''
        if self.currentPage >= self.pages:
            print('Книга завершена')
        else:
            print('Книга не завершена')
        
# book = Book('Буба Великий', 'Русин Саша', 120)
# print(book.currentPage)
# book.read(50)
# book.read(60)
# print(book.currentPage)
# book.isFinished()
# book.info()

# Задача 3: Библиотечная система 📚
# Условие:
# Создайте три класса: Book, Reader, и Library

# Класс Book:
# Атрибуты: title, author, isbn, is_borrowed (взята ли книга), borrower (кто взял)
# Методы:
# borrow(reader) — выдать книгу читателю
# return_book() — вернуть книгу в библиотеку
# info() — показать информацию о книге

class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.isBorrowed: bool = False
        self.borrower: Reader = None

    def borrow(self, reader: Reader):
        if self.isBorrowed:
            print('Книга уже взята')
        else:
            self.isBorrowed = True
            self.borrower = reader

    def returnBook(self):
        self.isBorrowed = False
        self.borrower = None
        print(f'Книгу {self.title} вернули')

    def info(self):
        print(f'Книга: {self.title} \n' \
              f'Автор: {self.author} \n' \
              f'isbn: {self.isbn}')
              

# Класс Reader:
# Атрибуты: name, reader_id, borrowed_books (список взятых книг), max_books (лимит книг)
# Методы:
# can_borrow() — проверяет, может ли взять ещё книги
# add_book(book) — добавляет книгу в список взятых
# remove_book(book) — удаляет книгу из списка
# show_books() — показывает все взятые книги

class Reader:
    def __init__(self, name: str, readerId: str, maxBooks: int):
        self.name = name
        self.readerId = readerId
        self.borrowedBooks: list[Book] = []
        self.maxBooks = maxBooks

    def canBorrow(self): 
        if len(self.borrowedBooks) >= self.maxBooks:
            return False
        else:
            return True

    def addBook(self, book: Book): 
        if self.canBorrow():
            self.borrowedBooks.append(book)
        else: 
            print('Нельзя взять больше книг')

    def removeBook(self, book: Book): 
        if book in self.borrowedBooks:
            self.borrowedBooks.remove(book)
        else:
            print('Такой книги нет')

    def showBooks(self): 
        for index, book in enumerate(self.borrowedBooks):
            print(f'{index + 1}. Книга {book.title}, автор: {book.author}')


# Класс Library:
# Атрибуты: books (список всех книг), readers (список читателей)
# Методы:
# add_book(book) — добавляет книгу в библиотеку
# register_reader(reader) — регистрирует читателя
# lend_book(isbn, reader_id) — выдаёт книгу читателю по ISBN и ID
# return_book(isbn) — принимает книгу обратно
# find_book_by_title(title) — ищет книгу по названию
# find_reader_by_id(reader_id) — ищет читателя по ID
# show_available_books() — показывает все доступные книги
# show_borrowed_books() — показывает все взятые книги

class Library:
    def __init__(self):
        self.books: list[Book] = []
        self.readers: list[Reader] = []

    def addBook(self, book: Book):
        self.books.append(book)

    def registerReader(self, reader: Reader):
        self.readers.append(reader)
    
    def lendBook(self, isbn: str, readerId: str):
        for book in self.books:
            if book.isbn == isbn:
                for reader in self.readers:
                    if reader.readerId == readerId:
                        book.borrow(reader)
                        reader.addBook(book)
                        print(f'Книга {book.isbn} выдана читателю {reader.readerId}')

    def returnBook(self, isbn: str):
        for reader in self.readers:
            for book in reader.borrowedBooks:
                if book.isbn == isbn:
                    reader.removeBook(book)
                    book.returnBook()
                    print(f'Книга {book.isbn} возвращена')

    def findBookByTitle(self, title: str):
        for book in self.books:
            if book.title == title:
                print(f'Книга {book.title}, автор: {book.author}, isbn: {book.isbn}')

    def findReaderById(self, readerId: int):
        for reader in self.readers:
            if reader.readerId == readerId:
                print(f'Читатель {reader.name}, id: {reader.readerId}')

    def showAvailableBooks(self):
        for book in self.books:
            if not book.isBorrowed:
                print(f'Книга {book.title}, автор: {book.author}, isbn: {book.isbn}')

    def showBorrowedBooks(self):
        for book in self.books:
            if book.isBorrowed:
                print(f'Книга {book.title}, автор: {book.author}, isbn: {book.isbn}')

library = Library()

book1 = Book("1984", "Orwell", "12345")
book2 = Book("Brave New World", "Huxley", "67890")
book3 = Book("Fahrenheit 451", "Bradbury", "11111")

reader1 = Reader("Alice", "R001", 3)
reader2 = Reader("Bob", "R002", 2)

library.addBook(book1)
library.addBook(book2)
library.addBook(book3)

library.registerReader(reader1)
library.registerReader(reader2)

library.lendBook("12345", "R001")
library.lendBook("67890", "R001")

library.showAvailableBooks()

library.showBorrowedBooks()

library.returnBook("12345")
reader1.showBooks()  