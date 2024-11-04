# Establish class for Authors

class Author:
  
    def __init__(self, name, biography):
        #make private attributes for author name and biography
    
        self.__name = name
      
        self.__biography = biography



# Menu Actions needed:
#Adding a new author with author details. 
#Viewing author details.
#Displaying a list of all authors. 



   #     Encapsulation:

#Apply encapsulation principles by defining private attributes 
# and using getters and setters for necessary data access.

      # getters and setters
   
    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_biography(self):
        return self.__biography

    def set_biography(self, new_biography):
        self.__biography = new_biography


def add_author(author_list):
    author_id = int(input("What's the new Library Id #? "))
    author_name = input("What's the new member's name? ")
    biography = input("Please provide a short biography: ")
    
    author_list.append(Author(author_id, author_name, biography)) 

def get_author_details(author_id):
        if author_id:
            print(f'Details for selected author: ')


def display_authors(author_list):
       
        print("Current authors:")
        for author in author_list:
            if author:
                print(author)