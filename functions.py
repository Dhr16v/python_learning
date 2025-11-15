# def greet():
#     print("hello workd")

# greet()

# def add_numbers(a, b):
#     result = a + b
#     print("Sum is:", result)

# add_numbers(5, 10)

# def greet(name="User"):
#     print(f"Hello, {name}!")

# greet("Dhruv")     # uses provided value
# greet()            # uses default value


def student_info(name,age):
    print(f"Name: {name}, Age: {age}")

student_info("Dhruv",21)

# Variable-Length Arguments

# Sometimes we don’t know how many arguments will be passed —
# we can handle that using *args and **kwargs.

def show_numbers(*args):
    print("Numbers:", args) #args is a tuple

show_numbers(1, 2, 3, 4, 5)

# *Example 2: kwargs (Keyword arguments)

def show_details(**kwargs):
    print("Details:", kwargs) #kwargs is a dictionary

show_details(name="Dhruv", age=21, city="Ahmedabad")

# Recursion (Function calling itself)

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

print('factorial of 5 is:',factorial(5))

x = 100   # global variable

def show_value():
    x = 50  # local variable
    print("Inside function:", x)

show_value()
print("Outside function:", x)

# Lambda Functions (Anonymous functions)
# Lambda functions are small anonymous functions that can have any number of arguments,

def square(x):
    return x**2

print('square of 5 is:',square(5))

#lamda function

square_lambda= lambda x:x**2
print('square of 5 is:',square_lambda(5))

#map function

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x:x**2,numbers))
print('squared numbers:',squared_numbers)

#filter function

nums=[1,2,3,4,5,6,7,8,9,10]

even_numbers = list(filter(lambda x:x%2==0,nums))
print('even numbers:',even_numbers)

#reduce function

from functools import reduce

nums=[1,2,3,4,5]

product = reduce(lambda x,y:x*y,nums)
print('product of numbers:',product)