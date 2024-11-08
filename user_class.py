
# Establish class for User

# Menu Actions needed:
#Adding a new user with user details. check
#Viewing user details.
#Displaying a list of all users. check

class User:
  
    def __init__(self, library_id, member_name, username, password):
        #make private attributes 
       
        self.__library_id = library_id
        self.__member_name = member_name 
        self.__username = username
        self.__password = password
       

    # getters and setters
    
   # Encapsulation:

#Apply encapsulation principles by defining private attributes and using 
# getters and setters for necessary data access.


    def get_library_id(self):
        return self.__library_id

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
    library_id = int(input("What's the new Library Id #? "))
    member_name = input("What's the new member's name? ")
    username = input("Please create a username. ")
    password= input("Please create a secure password: ")
    user_list[library_id] = User(library_id, member_name, username, password)

    print(f'User added! Current list of users: {user_list}')


def get_user_details(user_list, library_id):
        
        if library_id in user_list:
             print(f'User found! {user_list[library_id]}')
        else:
             print(f'User with id: {library_id} not found!')
            



def display_users(user_list):
       
    print("Current Users:")
    for user in user_list:
            if user:
                print(f'User id: {user.get_library_id()} \n Member name: {user.get_member()}')


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
          input_library_id = int(input("Enter the library id to get user details: "))
         
                
                

        elif choice == 3:
            display_users(user_list)
                
               