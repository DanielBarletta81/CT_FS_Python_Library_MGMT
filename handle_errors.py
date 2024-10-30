## errors.py

# class CustomError(Exception):
#    """Base class for custom exceptions."""
#    pass

# class InvalidInputError(CustomError):
#   """Raised when the input value is invalid."""
#   pass

# class DatabaseConnectionError(CustomError):
#    """Raised when there's an error connecting to the database."""
#    pass



class CustomError(Exception):
    pass

class InputError(CustomError):
 
    pass

def handle_error(error):
    print(f'Unfortunately, an error occurred {error}')