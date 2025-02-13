
def my_decorator(func):
    def wrapper():
        print("before call hello")
        func()
        print("after hello called")
    return wrapper
        

@my_decorator
def say_hello():
    print("Hello")
    
say_hello()