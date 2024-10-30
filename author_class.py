# Establish class for Authors

class Author:
  
    def __init__(self, name, biography):
        #make private attributes for author name and biography
    
        self.__name = name
      
        self.__biography = biography

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
