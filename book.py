#define a class Book with the following description
#Data members:
#bookname,bookid,authorid,authorname,price,booktitle
#Member methods:
#getauthorid(),getauthorname(),getbooktitle(),getprice(),setauthorname(),setbooktitle(),setprice()

class Book:
    def __init__(self):
        self.bookname=input('Enter the bookname:')
        self.bookid=int(input('Enter the book id:'))
        self.authorid=input('enter the author id:')
        self.authorname=input('Enter the author name:')
        self.price=int(input('Enter the price:'))
        self.booktitle =input('Enter the book title:')
    def getauthorid(self):
        print('Author id is:')
    def getauthorname(self):
        print('Author name is:')
    def getbooktitle(self):
        print('Book title is:')
    def getprice(self):
        print('Book price is:')
    def setauthorid(self):
        self.authorid=int(input('enter the new id:'))
        self.getauthorid()
    def setauthorname(self):
        self.authorname=int(input('enter the new id:'))
        self.getauthorname()
    def setbooktitle(self):
        self.booktitle= int(input('enter the new id:'))
        self.getbooktitle()
    def setprice(self):
        self.price = int(input('enter the new id:'))
        self.getprice()
b=Book()
b.setauthorname()
b.setbooktitle()
b.setprice()
b.setauthorid()