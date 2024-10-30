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

from classes import Book

def bookMenu():
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
                genre = int(input("Enter new book genre: "))
                title = input("Enter book title: ")
                author = int(input("Enter author id: "))
                date_published = input("Enter publication date: ")
                
       
            elif choice == 2:
                isbn = input('Enter the ISBN of the book: ')
                
                

            elif choice == 3:
                print(Book.book_list)
                


            elif choice == 4:
                
                user_id = int(input("Enter user id for borrowed book: "))
                book_id = int(input("Enter book id for borrowed book: "))
                borrow_date = input("What date was book borrowed? ")
                borrow_book(cursor, id, user_id, book_id, borrow_date)
                conn.commit()
                
       
            elif choice == 5:
               
                user_id = int(input("Enter user id for returned book: "))
                book_id = int(input("Enter book id for returned book: "))
                return_date = input("What date was book returned? ")
                
                
       
            else:
                 print("Invalid selection, please try again.")

        except Exception as e:
            print(f"An exception occurred: {e}")