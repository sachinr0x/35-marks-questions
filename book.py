class Book:

    def __init__(self, bookId, bookName, authorName):
        self.bookId= bookId
        self.bookName= bookName
        self.authorName= authorName
    

class Library(Book):

    def __init__(self, bookObject, libraryAddress):
        self.bookObject=bookObject
        self.libraryAddress= libraryAddress

    def findBookCountByAuthor(self):
        pass

def findBookByCity(cityName, libObj):
    pass

n= int(input())
libObj=[]
bookList=[]

for i in range (n):
    
    address={}

    bId= int(input())
    bName= input()
    bAuthor= input()
    bookList.append(Book(bId, bName, bAuthor))
    




 
# Input:

# 3
# 3
# 1
# Halmet
# shakesphere
# 2
# Macbeth
# SHAKESPHERE
# 3
# othrllo
# Shakesphere
# A-10
# gomtinagar
# lucknow
# u.p.
# 201876
# 3
# 1
# A Christmas Carol.
# Charies Dickens
# 2
# Bleak House
# Charies Dickens
# 3
# Oliver Twist
# Charies Dickens
# A-770
# rajamandi
# agara
# u.p.
# 2018763
# 3
# 1
# The adventures of sherlock holmes
# sherlock holmes
# 2
# The return of sherlock holmes
# sherlock holmes
# 3
# The sign of the four
# sherlock holmes
# A-660
# Khairatabad
# lucknow
# u.p.
# 201876
# lucknow   