from sys import stdin

if __name__ == "__main__":

  books_libraries_days = input().split
  book_scores = input().split

  libraries = []

  class Library:
    def __init__(self, library_data):
      self.num_books = int(library_data[0])
      self.num_signup_days = int(library_data[1])
      self.book_ship_rate = int(library_data[2])

  for line in stdin:
    libraries.append(Library(line))



  
    


