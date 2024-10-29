# 1. Create an improved, user-friendly command-line interface (CLI) for the Library Management
#  System with separate menus for each class of the system.


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

     choice = int(input("Please choose a menu. "))

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


main()   


