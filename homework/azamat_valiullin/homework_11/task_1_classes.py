class Book:
    page_material = "paper"
    text_availability = True

    def __init__(self, title, author, number, isbn, availability=None):
        self.title = title
        self.author = author
        self.number = number
        self.isbn = isbn
        self.availability = availability


book_1 = Book("Idiot", "Dostoevsky", 500, 978 - 5 - 7320 - 1162 - 3)
book_2 = Book("The Great Gatsby", "F. Scott Fitzgerald", 700, 978 - 5 - 4820 - 1162 - 3)
book_3 = Book("Uncle Tom's Cabin", "Harriet Elizabeth Beecher Stowe", 435, 858 - 5 - 7320 - 11624)
book_4 = Book("Dead Souls", "Nikolai Gogol", 850, 978 - 5 - 7320 - 8962 - 3, True)
book_5 = Book("Anna Karenina", "Leo Tolstoy", 900, 898 - 5 - 7320 - 1162 - 3)

book_list = [book_1, book_2, book_3, book_4, book_5]

for book in book_list:
    if book.availability:
        print(
            f"Title: {book.title}, Author: {book.author}, "
            f"pages: {book.number}, material: {book.page_material}, reserved"
        )
    else:
        print(f"Title: {book.title}, Author: {book.author}, pages: {book.number}, material: {book.page_material}")


class SchoolBooks(Book):

    def __init__(self, title, author, number, isbn, subject, group, task=True, availability=None):
        super().__init__(title, author, number, isbn, availability)
        self.subject = subject
        self.group = group
        self.task = task


school_book_1 = SchoolBooks(
    "Algebra", "Ivanov", 350, 978-5-7320-1162-3, "Mathematics",
    "9", True, True
)

school_book_2 = SchoolBooks(
    "History", "Sidorov", 450, 111-5-7320-1162-3, "History",
    9, True
)

school_book_3 = SchoolBooks(
    "Biology", "Petrov", 280, 978-5-7320-1162-3, "Biology",
    9, True
)

school_book_list = [school_book_1, school_book_2, school_book_3]

print("*" * 100)

for book in school_book_list:
    if book.availability:
        print(f"Title: {book.title}, Author: {book.author}, pages: {book.number}, subject: {book.subject} reserved ")
    else:
        print(f"Title: {book.title}, Author: {book.author}, pages: {book.number}, subject: {book.subject}")
