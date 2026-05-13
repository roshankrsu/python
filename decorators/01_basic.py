from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before funtion runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator
def greet():
    print("Hello, how are you?")

greet()
print(greet.__name__)