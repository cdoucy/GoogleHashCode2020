BOOK_SCORE = []

class Library(object):
    def __init__(self, ID, nb_books, days, m):
        self.ID = ID
        self.books = []
        self.nb_books = nb_books
        self.days = days
        self.m = m
        self.calcDays()
        self.calcScore()

    def addBook(self, book):
        self.books.append(book)

    def calcDays(self):
        self.tot_days = self.days + self.nb_books / self.m

    def calcScore(self):
        self.tot_score = 0
        for it in self.books:
            self.tot_score += BOOK_SCORE[it.books]

class BookScanning(object):
    def __init__(self, total_books, nb_libs, nb_days, books_scores):
        self.total_books = total_books
        self.nb_libs = nb_libs
        self.nb_days = nb_days
        self.libs = []
        self.books_scores = books_scores

def algo(bs):
    x = 0
    # bs.libs.sort(key = lambda x: x.tot_days, reverse = True)
    # bs.libs.sort(key = lambda x: x.days, reverse = False)
    bs.libs.sort(key = lambda x: x.tot_score, reverse = True)
    print(bs.nb_libs)
    for it in bs.libs:
        print(it.ID, it.nb_books)
        print(str(it.books)[1: -1].replace(',', ''))
        x += 1

def parseHeader(first, second):
    books_scores = []

    split = first.split()
    total_books = int(split[0])
    nb_libs = int(split[1])
    nb_days = int(split[2])
    split = second.split()
    for it in split:
        books_scores.append(int(it))
    BOOK_SCORE = books_scores
    return BookScanning(total_books, nb_libs, nb_days, books_scores)

def parse(filepath):
    fd = open(filepath, "r")
    lines = fd.readlines()
    bs = parseHeader(lines[0], lines[1])
    x = 0
    for i in range(2, len(lines), 2):
        split = lines[i].split()
        l = Library(x, int(split[0]), int(split[1]), int(split[2]))
        x += 1
        split = lines[i + 1].split()
        for it in split:
            l.addBook(int(it))
        bs.libs.append(l)
    return bs

if __name__ == "__main__":
    from sys import argv
    bs = parse(argv[1])
    # print(bs.total_books, bs.nb_libs, bs.nb_days, bs.books_scores)
    algo(bs)
    # for it in bs.libs:
    #     print(it.nb_books, it.days, it.m, it.books)
