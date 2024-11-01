
# Establish class for User

# Menu Actions needed:
#Adding a new user with user details. check
#Viewing user details.
#Displaying a list of all users. check

class User:
  
    def __init__(self, library_id, first_name, last_name, username, password, bookList):
        #make private attributes 
        self.users_list = []
        self.__library_id = library_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__username = username
        self.__password = password
        self.__bookList = bookList

    # getters and setters
    
   # Encapsulation:

#Apply encapsulation principles by defining private attributes and using 
# getters and setters for necessary data access.


    def get_library_id(self):
        return self.__library_id

    def set_library_id(self, new_library_id):
        self.__library_id = new_library_id


    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, new_first_name):
        self.__first_name = new_first_name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, new_last_name):
        self.__last_name = new_last_name

    def get_username(self):
        return self.__username

    def set_username(self, new_username):
        self.__username = new_username

    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        self.__password = new_password

    def get_bookList(self):
        return self.__bookList

    def set_bookList(self, new_bookList):
        self.__bookList = new_bookList

    def add_user(self, library_id, first_name, last_name, username, password):
        new_user = (library_id, first_name, last_name, username, password)
        self.users_list.append(new_user)
        print(self.items)

    def get_user_details(self, library_id):
        if library_id:
            print(User)


    def display_users(self):
       
        print("Current Users:")
        for user in self.users_list:
            if user:
                print(user)

