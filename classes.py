# Create Classes here 
#
#
#
class Author:
  
    def __init__(self, name, biography):
        #make private attributes for author name and biography
    
        self.__name = name
      
        self.__biography = biography

   #     Encapsulation:

#Apply encapsulation principles by defining private attributes 
# and using getters and setters for necessary data access.

      # getters and setters
   
    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_biography(self):
        return self.__biography

    def set_biography(self, new_biography):
        self.__biography = new_biography


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


class User:
  
    def __init__(self, library_id, first_name, last_name, username, password, bookList):
        #make private attributes for author name and username, password
        self.__library_id = library_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__username = username
        self.__password = password
        self.__bookList = bookList

    # getters and setters
    
   # Encapsulation:

#Apply encapsulation principles by defining private attributes and using 
# getters and setters for necessary data access.


    def get_library_id(self):
        return self.__library_id

    def set_library_id(self, new_library_id):
        self.__library_id = new_library_id


    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, new_first_name):
        self.__first_name = new_first_name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, new_last_name):
        self.__last_name = new_last_name

    def get_username(self):
        return self.__username

    def set_username(self, new_username):
        self.__username = new_username

    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        self.__password = new_password

    def get_bookList(self):
        return self.__bookList

    def set_bookList(self, new_bookList):
        self.__bookList = new_bookList



