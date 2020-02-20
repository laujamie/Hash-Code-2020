from sys import stdin


class Library:
    def __init__(self, library_data, books):
        self.num_books = int(library_data[0])
        self.num_signup_days = int(library_data[1])
        self.book_ship_rate = int(library_data[2])
        self.books = books


if __name__ == "__main__":

    books_libraries_days = input().split()
    book_scores = input().split()

    print(books_libraries_days)
    print(book_scores)

    libraries = []

    while True:
        try:
            library_data = input().split()
            library_books = input().split()
            libraries.append(Library(library_data, library_books))
        except EOFError:
            break
    
    print(libraries)
