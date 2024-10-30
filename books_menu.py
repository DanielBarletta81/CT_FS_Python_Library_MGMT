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

from book_class import Book

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
                pass
                
       
            elif choice == 2:
                pass
                
                

            elif choice == 3:
               pass
                


            elif choice == 4:
                
                pass
       
            elif choice == 5:
                pass
               
  #      user_id = int(input("Enter user id for returned book: "))
   #     book_id = int(input("Enter book id for returned book: "))
    #    return_date = input("What date was book returned? ")
                

        except Exception as e:
                 print(f"An exception occurred: {e}")