## main entry point

# 1. Create an improved, user-friendly command-line interface (CLI) for the Library Management
#  System with separate menus for each class of the system.
from book_class import bookMenu
from user_class import userMenu
from author_class import authorMenu

"""     Welcome to the Library Management System!

    Main Menu:
    1. Book Operations
    2. User Operations
    3. Author Operations
    4. Quit """

## main menu



def main():
  while True:
    
     print("***  Welcome to the Library Management System!  ***")
     print("\n Menu: ")
     print("\n 1. Book Operations. ")
     print("\n 2. User Operations. ")
     print("\n 3. Author Operations. ")
     print("\n 4. Quit. ")

     choice = int(input("Please choose an option. "))

     if choice == 4:
        return
     elif choice == 1:
        bookMenu()
     elif choice == 2:
        userMenu()
     elif choice == 3:
        authorMenu()
        
     
     else:
        print("Error, invalid input. ")


main()   
