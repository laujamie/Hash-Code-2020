from sys import stdin

books = []
scanned_books = []
book_scores = []


class Library:
    def __init__(self, id, library_data, books):
        self.num_books = int(library_data[0])
        self.num_signup_days = int(library_data[1])
        self.book_ship_rate = int(library_data[2])
        self.books = books
        self.books.sort(key=self.sort_books, reverse=True)
        self.registered = False
        self.id = id

    def sort_books(self, index):
        return book_scores[index]


if __name__ == "__main__":

    books_libraries_days = list(map(int, input().split()))
    book_scores = list(map(int, input().split()))

    libraries = []

    i = 0
    while True:
        try:
            library_data = list(map(int, input().split()))
            library_books = list(map(int, input().split()))
            libraries.append(Library(i, library_data, library_books))
            i += 1
        except EOFError:
            break

print(libraries[0].books, libraries[1].books)
print(book_scores)
print(libraries[0].books, libraries[1].books)
