
class IllegalInputError(Exception):
    def __init__(self, message):
        self.message = f"Input should be poker number: {message}"

class MethodChooseError(Exception):
    def __init__(self, message):
        self.message = f"Method should be exist: {message}"

def except_decorator(func):
    def wrapper(*args, **kargs):
        try:
            return func(*args, **kargs)
        except IllegalInputError as e:
            print(f"{e.__class__.__name__}: {e.message}")
            print("維持上一把的 desicion......")
        except MethodChooseError as e:
            print(f"{e.__class__.__name__}: {e.message}")
            exit()
        except Exception as e:
            print(f"Error: {e}")
    return wrapper