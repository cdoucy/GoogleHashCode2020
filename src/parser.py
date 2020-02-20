class Library(object):
    def __init__(self, nb_books, days, m):
        self.books = []
        self.nb_books = nb_books
        self.days = days
        self.m = m

    def addBook(self, book):
        self.books.append(book)

class BookScanning(object):
    def __init__(self, total_books, nb_libs, nb_days, books_scores):
        self.total_books = total_books
        self.nb_libs = nb_libs
        self.nb_days = nb_days
        self.libs = []
        self.books_scores = books_scores

def parseHeader(first, second):
    books_scores = []

    split = first.split()
    total_books = int(split[0])
    nb_libs = int(split[1])
    nb_days = int(split[2])
    split = second.split()
    for it in split:
        books_scores.append(int(it))
    return BookScanning(total_books, nb_libs, nb_days, books_scores)

def parse(filepath):
    fd = open(filepath, "r")
    lines = fd.readlines()
    bs = parseHeader(lines[0], lines[1])
    for i in range(2, len(lines), 2):
        split = lines[i].split()
        l = Library(int(split[0]), int(split[1]), int(split[2]))
        split = lines[i + 1].split()
        for it in split:
            l.addBook(int(it))
        bs.libs.append(l)
    return bs

if __name__ == "__main__":
    from sys import argv
    bs = parse(argv[1])
    print(bs.total_books, bs.nb_libs, bs.nb_days, bs.books_scores)
    for it in bs.libs:
        print(it.nb_books, it.days, it.m, it.books)
