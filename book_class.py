# Create Classes here 




#Book Operations:
#        Book Operations:
#        1. Add a new book
#        2. Borrow a book
 #       3. Return a book
  #      4. Search for a book
    #    5. Display all books
# Menu Actions:

#Implement the following actions in response to menu selections using the classes
#  you've created:


#Adding a new book with all relevant details.
#Allowing users to borrow a book, marking it as "Borrowed."
#Allowing users to return a book, marking it as "Available."
#Searching for a book by its unique identifier (title) and displaying its details.
#Displaying a list of all books with their unique identifiers.
#
from handle_errors import CustomError, InputError
#
class Book:

    
  
    def __init__(self, title, author, genre, isbn):
        #make private attributes for genre and author
        
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__isbn = isbn
        
        self.__isAvailable = True

#Apply encapsulation principles by defining private attributes 
# and using getters and setters for necessary data access.

    # getters and setters
   
    def get_title(self):
        return self.__title

    def is_available(self):
        return self.__isAvailable

    def borrow_book(self):
        if self.__isAvailable:
            self.__isAvailable = False
            return True
        return False
    
    def return_book(self):
        self.__isAvailable = True



def add_book(library): # library will be a dictionary
        
        title = input("Enter the book title: ")
        author = input("Enter the author's name: ")
        genre = input("Enter the book genre: ")
        isbn = input("Enter the ISBN: ")
        library[isbn] = Book( title, author, genre, isbn)
      

def check_out_book(library, current_loans):
     isbn = input("Enter the ISBN of book being borrowed: ")
     user = input("Enter the user borrowing book: ")
     if isbn in library and library[isbn].borrow_book():
          current_loans[isbn] = user
          print(f'Book {library[isbn].get_title()} checked out by {user}. ')
     else:
          print("That book is not available, or not found in library. ")

def check_in_book(library, current_loans):
     isbn = input("Enter the ISBN of book being returned: ")
     if isbn in library and isbn in current_loans:
          library[isbn].return_book()
          del current_loans[isbn]
          print(f'Book {library[isbn].get_title()} returned. ')
     else:
          print("The book ISBN is invalid or the book was not borrowed. ")


def find_book(library):
     isbn = input("Enter the ISBN of book to search library: ")
     if isbn in library:
          print(f'Book with ISBN {isbn} found! Title: {library[isbn].get_title()}')

def display_entire_library(library):
     for book in library:
          print(f' ISBN: {book} \n Title: {library[book].get_title()} \n')
          

## add Book menu


def bookMenu():
     library = {}
     current_loans = {}
     while True:
    
        print("***  Welcome to the Library's Book Menu!  ***")
        print("\n Menu: ")
        print("\n 1. Add a Book. ")
        print("\n 2. Borrow a book. ")
        print("\n 3. Return a book. ")
        print("\n 4. Search for a book. ")
        print("\n 5. Display all Books. ")
        print("\n 6. Return to Main Menu. ")

        choice = int(input("What would you like to do (1-6)? "))

        if choice == 6:
            return
        
        try:
            

            if choice == 1:
                add_book(library)
                
       
            elif choice == 2:
                check_out_book(library, current_loans)
                

            elif choice == 3:
                check_in_book(library, current_loans)
                

            elif choice == 4:
                find_book(library)
       
            elif choice == 5:
                display_entire_library(library)
               

        except Exception as e:
                 print(f"An exception occurred: {e}")
