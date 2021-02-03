# Create a Book class
class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        return "Name: " + self.name + " Author: " + self.author
    
    def __repr__(self):
        return "Name: " + self.name + " Author: " + self.author


#Create a Backpack class
class Backpack:
    def __init__(self, books):
        self.books = books

    def __str__(self):
        return books.__str()

    def __repr__(self):
        return books.__str()

    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        if (self.x < len(self.books)):
            current_book = self.books[self.x]
            self.x = self.x+1
            return current_book
        else:
            raise StopIteration


# Create some books
b1 = Book("Harry Potter", "J.K. Rowling")
b2 = Book("Percy Jackson", "Rick Riordan")
b3 = Book("House Rules", "Jodi Picoult")
b4 = Book("Hamlet", "William Shakespeare")
#create a list of books
books = [b1,b2,b3,b4]

# Create a Backpack
backpack_1 = Backpack(books)

# Using a for loop 
print("--> Calling internal iterator")
for x in backpack_1:
    print(x)

# Using an iterator object explictly
iterator_x = iter(backpack_1)
print("--> Calling explit iterator")
print(next(iterator_x))
print(next(iterator_x))
print(next(iterator_x))
print(next(iterator_x))

