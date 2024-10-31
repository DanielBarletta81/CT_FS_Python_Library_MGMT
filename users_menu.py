from user_class import add_user
# 
#          User Operations:
        
#           1. Add a new user
 #          2. View user details
 #          3. Display all users
#
#
#
def userMenu():
     while True:
    
        print("***  Welcome to the Library's User Menu!  ***")
        print("\n Menu: ")
        print("\n 1. Add a user. ")
        print("\n 2. View user information. ")
        print("\n 3. Display all users. ")
        print("\n 4. Return to Main Menu. ")

        choice = int(input("What would you like to do (1-6)? "))

        if choice == 4:
            return
        
        elif choice == 1:
            add_user()
                
       
        elif choice == 2:
            pass
                
                

        elif choice == 3:
            pass
                
               