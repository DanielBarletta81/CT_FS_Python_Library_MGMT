# Establish class for Authors

class Author:
  
    def __init__(self, author_id,  author_name, biography):
        #make private attributes for author name and biography

        self.__author_id = author_id
        self.__author_name = author_name
      
        self.__biography = biography



# Menu Actions needed:
#Adding a new author with author details. 
#Viewing author details.
#Displaying a list of all authors. 



   #     Encapsulation:

#Apply encapsulation principles by defining private attributes 
# and using getters and setters for necessary data access.

      # getters and setters
   
    def get_author_name(self):
        return self.__author_name

    
    def get_biography(self):
        return self.__biography



def add_author(author_list):
    author_id = int(input("What's the new Author Id #? "))
    author_name = input("What's the new author's name? ")
    biography = input("Please provide a short biography: ")
    author_list[author_id] = Author(author_id, author_name, biography)

    print(f' New author added:  {author_name}')
    
     

def get_author_details(author_list):
        author_id = int(input("Please enter the author id: "))
        if author_id in author_list:
            print(f'Details for selected author: {author_list[author_id].get_author_name()} from their biography: {author_list[author_id].get_biography()}') 
            


def display_authors(author_list):
       
        print("Current authors:")
        for author in author_list:
            if author:
                print(f'Author ID: {author} \n Name: {author_list[author].get_author_name()}')

"""  Author Operations:
        1. Add a new author
        2. View author details
        3. Display all authors """

def authorMenu():
     author_list = {}
     while True:
    
        print("***  Welcome to the Library's Author Menu!  ***")
        print("\n Menu: ")
        print("\n 1. Add an author. ")
        print("\n 2. View author information. ")
        print("\n 3. Display all authors. ")
        print("\n 4. Return to Main Menu. ")

        choice = int(input("What would you like to do (1-4)? "))

        if choice == 4:
            return
        
        elif choice == 1:
            add_author(author_list)
                
        elif choice == 2:
            get_author_details(author_list)
                
        elif choice == 3:
            display_authors(author_list)