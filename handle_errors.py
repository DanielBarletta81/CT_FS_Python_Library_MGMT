## Module for error handling


class CustomError(Exception):
    pass

class InputError(CustomError):
 
    pass

def handle_error(error):
    print(f'Unfortunately, an error occurred: {error}')