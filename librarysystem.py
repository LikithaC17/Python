class Library:
    def __init__(self):
        self.books=["Python","Java","C"]
    def show(self):
        print(self.books)
    def issue(self,book):
        if book in self.books:
            self.books.remove(book)

l=Library()
l.show()
l.issue("Python")
l.show()