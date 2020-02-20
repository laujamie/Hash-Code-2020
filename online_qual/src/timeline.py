from functools import reduce


class Timeline():
    def __init__(self, libraries, book_scores):
        self.timeline = []
        self.libraries = libraries
        self.book_scores = book_scores
        self.registered_libs = []
        self.all_libs = libraries[:]
        self.books_sent_so_far = set([])

    def send_books(self, index):
        library = self.all_libs[index]
        to_send = []
        for book in library.books:
            if book in self.books_sent_so_far:
                continue
            if len(to_send) == library.book_ship_rate:
                break

            to_send.append(book)
            self.books_sent_so_far.add(book)

        return to_send

    def library_score(self, library):
        return sum(self.book_scores[i] for i in library.books) / (
            library.num_signup_days +
            library.num_books / library.book_ship_rate)

    def rank_libraries(self, libraries):
        libraries.sort(key=lambda x: self.library_score(x))
        return libraries

    def newDay(self, actions):
        res = {}
        for action in actions:
            res[action[0]] = action[1]
        self.timeline.append(res)

    def generateActions(self):
        prev_day = self.timeline[-1] if self.timeline else {}
        res = []
        if prev_day:
            for i, j in prev_day.items():
                if isinstance(j, int):
                    if not j:
                        try:
                            self.registered_libs.append(self.libraries[0])
                            self.libraries = self.libraries[1:]
                        except:
                            print('Jeffrey is crazy')
                        books = self.send_books(i)
                        res.append((i, books))
                        # register a new library
                        self.rank_libraries(self.libraries)
                        try:
                            res.append((self.libraries[0].id,
                                        self.libraries[0].num_signup_days - 1))
                        except:
                            print('list empty')
                    else:
                        temp = (i, j - 1)
                        res.append(temp)
                if isinstance(j, list):
                    lib = next(lib for lib in self.registered_libs if lib.id == i)
                    books = self.send_books(i)
                    for b in books:
                        lib.sent_books.append(b)
                    res.append((i, books))
        else:
            self.rank_libraries(self.libraries)
            res.append(
                (self.libraries[0].id, self.libraries[0].num_signup_days - 1))
        self.newDay(res)

    def print(self):
        output = []
        output.append(len(self.registered_libs))
        for lib in self.registered_libs:
            output.append(f"{lib.id} {len(lib.sent_books)}")
            temp = ""
            for b in lib.sent_books:
                temp += f"{b} "
            output.append(temp)
        with open("output.txt", "w+") as f:
            for line in output:
                print(line, file=f)
