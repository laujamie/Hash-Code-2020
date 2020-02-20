from sys import stdin

from .timeline import Timeline

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
        self.sent_books = []

    def sort_books(self, index):
        return book_scores[index]


if __name__ == "__main__":

    num_books, num_libraries, num_days = tuple(map(int, input().split()))
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

    timeline = Timeline(libraries, book_scores)
    for i in range(num_days):
        timeline.generateActions()

    timeline.print()
