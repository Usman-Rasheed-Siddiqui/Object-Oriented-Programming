
class Book:
    def __init__(self, isbn, title, authors=[], genre=None):
        self.isbn = isbn
        self.title = title
        self.author = authors
        self.genre = genre

    def set_genre(self, g):
        if not self.genre:
            self.genre = g

    def add_author(self, an):
        self.author.append(an)

B1 = Book(2403, "Goosebumps")
B1.set_genre("horror")
B1.add_author("RL Stine")
B1.add_author("Usman")
print(B1.author)
