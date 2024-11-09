
# Establish class for User

# Menu Actions needed:
#Adding a new user with user details. check
#Viewing user details.
#Displaying a list of all users. check

class User:
  
    def __init__(self, user_id, member_name, username, password):
        #make private attributes 
       
        self.__user_id = user_id
        self.__member_name = member_name 
        self.__username = username
        self.__password = password
       

    # getters and setters
    
   # Encapsulation:

#Apply encapsulation principles by defining private attributes and using 
# getters and setters for necessary data access.


    def get_user_id(self):
        return self.__user_id

 #   def set_library_id(self, new_library_id):
  #      self.__library_id = new_library_id


    def get_member(self):
        return self.__member_name

  #  def set_member(self, new_member_name):
  #      self.__member_name = new_member_name

    def get_username(self):
        return self.__username

  #  def set_username(self, new_username):
  #      self.__username = new_username

    def get_password(self):
        return self.__password

  #  def set_password(self, new_password):
   #     self.__password = new_password

        #user functions below  VVVV


def add_user(user_list):
    user_id = int(input("What's the new user Id #? "))
    member = input("Enter the name on account: ")
    user_name = input("Please create a username: ")
    password = input("Enter a secure password: ")
    
   
    user_list[user_id] = User(user_id, member, user_name, password)

    print(f' New user added:  {user_name}')
    
     

def get_user_details(user_list):
        user_id = int(input("Please enter the user id: "))
        if user_id in user_list:
            print(f'Details for selected user: Username: {user_list[user_id].get_username()} Member: {user_list[user_id].get_member()}') 
            


def display_users(user_list):
       
        print("Current users:")
        for user in user_list:
            if user:
                print(f'user ID: {user} \n Username: {user_list[user].get_username()} \n {user_list[user].get_member()}')



# 
#          User Operations:
        
#           1. Add a new user
 #          2. View user details
 #          3. Display all users
#
#
#
def userMenu():
     user_list = {}
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
          display_users(user_list)
         
                
        elif choice == 3:
            display_users(user_list)
                
               