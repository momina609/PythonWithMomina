# Decorator is a function that takes another function as an argument and returns a function.
# we put another func inside this  decorator ,this func performs the our original function and returns the func 
def decorator(func):
    def wrapper():
        print("transaction initiated")
        func()
        print("completed initiated")
        return wrapper
def hello():
    print("executing all steps of transaction...")
hello1=decorator(hello)# call of decorator
hello1()
# we can directly call decorator
@decorator
def hello():
    print("transaction execution")
hello()
#A decorator is a function that modifies the behavior of another function — without changing its actual code.
#It's used with the @ symbol
#Add functionality 
#Keep code clean and reusable
#example without decorator
def greet():
    print("Hello, Momina!")

greet()
# with decorator
def decorator(func):
    def wrapper():
        print("before the function runs...")
        func()
        print("after the function runs...")
        return wrapper()
@decorator
def greet():
    print("hellow!")
greet()
#@decorator is the same as:
#greet = decorator(greet)
#💡 Decorators with Arguments:
def decorator(func):
    def wrapper(*args,**kwargs):
        print("before func...")
        result=func(*args,**kwargs)
        print("after func...")
        return result
    return wrapper
@decorator
def add(a,b):
    return a+b
print(add(3,4))
#🔐 Use Case: Authorization Decorator
def authorize(func):
    def wrapper(user):
        if user=="admin":
            return func(user)
        else:
            print("excess denied.....")
    return wrapper
@authorize
def dashboard(user):
    return f"Welcome,{user}"
print(dashboard("admin"))
print(dashboard("user"))

