from user_class import User
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

        choice = int(input("What would you like to do (1-4)? "))

        if choice == 4:
            return
        
        elif choice == 1:
           
            User.add_user()
                
       
        elif choice == 2:
            User.get_user_details()
                
                

        elif choice == 3:
            User.display_users()
                
               