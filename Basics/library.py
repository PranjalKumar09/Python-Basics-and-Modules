class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []
        
    def addBook(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)
    def showInfo(self):
        print(f"The Library has {self.noBooks}. The Books are")
        for i in self.books:
            print(i)
        
l1 = Library()
l1.addBook("Harry Potter")
l1.addBook("Harry Potter1")
l1.addBook("Harry Potter2")
l1.addBook("Harry Potter3")
l1.showInfo