
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

class Catalog:
    catalog_count = 0

    def __init__(self, Book=[]):
        self.load_catalog_count()
        Catalog.catalog_count += 1
        self.cat_id = Catalog.catalog_count
        self.books = Book
        self.save_catalog_count()


    def save_catalog_count(self):
        with open("CatNo.txt" ,"w") as file:
            file.write(str(Catalog.catalog_count))

    def load_catalog_count(self):
        with open("CatNo.txt" ,"r") as file:
            read = file.read().strip()
            Catalog.catalog_count = int(read) if read else 0

    def add_book(self,i, t, an, g):
        book = Book(i, t, an, g)
        self.books.append(book)

# Example Usage
catalog = Catalog()
catalog.add_book(1234, "Python Programming",["John Doe"] ,"Education" )
catalog.add_book(5678, "Machine Learning Basics",["Jane Smith", "Alice Brown"] ,"Technology" )
print("Catalog ID:",catalog.catalog_count)
# Displaying stored books
for book in catalog.books:
    print(f"ISBN: {book.isbn}, Title: {book.title}, Authors: {book.author}, Genre: {book.genre}")
