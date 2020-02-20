from sys import stdin

books = []
scanned_books = []

def library_score(library):
  return sum(book_scores[i] for i in library.books)/(library.num_signup_days+library.num_books/library.book_ship_rate)


def rank_libraries(libraries):
  libraries.sort(key=lambda x:library_score(x))
  return libraries


class Library:
    def __init__(self, library_data, books):
        self.num_books = int(library_data[0])
        self.num_signup_days = int(library_data[1])
        self.book_ship_rate = int(library_data[2])
        self.books = books


if __name__ == "__main__":

    books_libraries_days = list(map(int, input().split()))
    book_scores = list(map(int, input().split()))

    libraries = []

    while True:
        try:
            library_data = list(map(int, input().split()))
            library_books = list(map(int, input().split()))
            libraries.append(Library(library_data, library_books))
        except EOFError:
            break

print(libraries[0].books, libraries[1].books)
print(book_scores)
rank_libraries(libraries)
print(libraries[0].books, libraries[1].books)
