
# Establish class for User

# Menu Actions needed:
#Adding a new user with user details. check
#Viewing user details.
#Displaying a list of all users. check

class User:
  
    def __init__(self, library_id, member_name, username, password, bookList):
        #make private attributes 
        self.users_list = []
        self.__library_id = library_id
        self.__member_name = member_name 
        self.__username = username
        self.__password = password
        self.__bookList = bookList

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

    def get_bookList(self):
        return self.__bookList

    def set_bookList(self, new_bookList):
        self.__bookList = new_bookList

        #user functions below  VVVV


def add_user(new_user):
    library_id = int(input("What's the new Library Id #? "))
    member_name = input("What's the new member's name? ")
    username = input("Please create a username. ")
    password= input("Please create a secure password: ")
        

    new_user[library_id] = User(library_id, member_name, username, password, bookList=[])
        
        
    print(f'New user added: {new_user}')

def get_user_details(self, library_id):
        library_id = int(input("Enter the library id to get user details: "))
        if library_id == self.__library_id:
             print(f'User found!')
            



def display_users(self):
       
    print("Current Users:")
    for user in self.users_list:
            if user:
                print(user)

