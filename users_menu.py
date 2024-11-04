from user_class import add_user, get_user_details, display_users
# 
#          User Operations:
        
#           1. Add a new user
 #          2. View user details
 #          3. Display all users
#
#
#
def userMenu():
     user_list = []
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
          add_user(user_list)
                
       
        elif choice == 2:
          input_library_id = int(input("Enter the library id to get user details: "))
          get_user_details(user_list, input_library_id)
                
                

        elif choice == 3:
            display_users(user_list)
                
               