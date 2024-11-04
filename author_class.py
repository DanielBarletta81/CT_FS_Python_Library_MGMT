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


    def add_author(self, , biography):
        new_author = 
        self.authors_list.append(new_author)
        print(self.items)

    def get_author_details(self, library_id):
        if library_id:
            print(f'Details for selected author: ')


    def display_authors(self):
       
        print("Current authors:")
        for author in self.authors_list:
            if author:
                print(author)