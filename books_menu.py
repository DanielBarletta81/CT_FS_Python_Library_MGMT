#Book Operations:
#        Book Operations:
#        1. Add a new book
#        2. Borrow a book
 #       3. Return a book
  #      4. Search for a book
    #    5. Display all books

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

        if choice == 4:
            return
        elif choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            pass
     
        else:
            print("Error, invalid input. ")


