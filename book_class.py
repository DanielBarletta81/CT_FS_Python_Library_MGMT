# Create Classes here 
#
from handle_errors import CustomError, InputError
#
class Book:

    
  
    def __init__(self, title, genre, author, date_published, isAvailable):
        #make private attributes for genre and author
        self.__genre = genre
        self.__title = title
        self.__author = author
        self.__date_published = date_published
        self.__isAvailable = isAvailable

#Apply encapsulation principles by defining private attributes 
# and using getters and setters for necessary data access.

    # getters and setters
   
    def get_genre(self):
        return self.__genre

    def set_genre(self, new_genre):
        self.__genre = new_genre
    
    def get_title(self):
        return self.__title

    def set_title(self, new_title):
        self.__title = new_title

    def get_author(self):
        return self.__author

    def set_author(self, new_author):
        self.__author = new_author

    def get_date_published(self):
        return self.__date_published

    def set_date_published(self, new_date_published):
        self.__date_published = new_date_published

    def get_isAvailable(self):
        return self.__isAvailable

    def set_isAvailable(self, new_isAvailable):
        self.__isAvailable = new_isAvailable

        

class Catalog:
    def __init__(self):
        self.books = []
        ## functions for book operations below VVVV

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def display_available_books(self):
        print("Available books:")
        for book in self.books:
            if book.isAvailable:
                print(book)


## functions for book operations below VVVV


      

        

