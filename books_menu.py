#Book Operations:
#        Book Operations:
#        1. Add a new book
#        2. Borrow a book
 #       3. Return a book
  #      4. Search for a book
    #    5. Display all books

class Book:
  
    def __init__(self, title, genre, author, date_published, isAvailable):
        #make private attributes for genre and author
        self.__genre = genre
        self.__author = author
        self.title = title
        self.date_published = date_published
        self.isAvailable = isAvailable

#Apply encapsulation principles by defining private attributes 
# and using getters and setters for necessary data access.

    # getters and setters
    def get_genre(self):
        return self.__genre

    def set_genre(self, new_genre):
        self.__genre = new_genre

    def get_author(self):
        return self.__author

    def set_author(self, new_author):
        self.__author = new_author


