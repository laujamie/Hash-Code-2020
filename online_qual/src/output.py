class Timeline():
    def __init__(self, libraries, book_scores):
        self.timeline = []
        self.libraries = libraries
        self.book_scores = book_scores
        self.registered_libs = []

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
            res[action[1]] = action[2]
        self.timeline.append(res)

    def generateActions(self):
        prev_day = self.timeline[-1] if self.timeline else []
        res = []
        for i, j in prev_day:
            if isinstance(j, int):
                if not j:
                    try:
                        self.registered_libs.append(self.libraries[0])
                        self.libraries = self.libraries[1:]
                    except:
                        print('Jeffrey is crazy')
                    # some call to add new books
                    # register a new library
                    self.rank_libraries(self.libraries)
                    try:
                        res.append(self.libraries[0].id,
                                   self.libraries[0].num_signup_days)
                    except:
                        print('list empty')
                else:
                    temp = (self.libraries[i].id, j - 1)
                    res.append(temp)
            if isinstance(j, list):
                print('Not working yet')
                # some function call to add more books
        if not prev_day:
            self.rank_libraries(self.libraries)
            res.append(
                (self.libraries[0].id, self.libraries[0].num_signup_days))
        self.newDay(res)
