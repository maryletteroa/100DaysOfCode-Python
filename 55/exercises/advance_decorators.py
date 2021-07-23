# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        result = function(*args)
        print(f"Function name: {function.__name__}, arguments: {args} ")
        print(f"Result: {result}")
    return wrapper

# Use the decorator 👇
@logging_decorator
def sum(n1, n2):
    return n1 + n2
# Call function
sum(3,2)
