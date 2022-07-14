# *args and **kwargs

# *args is like an argument collector. It collects all of the positional arguments passed into a function
# and stores them in a tuple called args. If you specify *args as a parameter for a function, you can 
# pass in as many positional arguments to your function as you want and access them through the args variable.

# Similarly, **kwargs is a keyword argument collector. **kwargs will collect all of the 
# keyword arguments and store them in a dictionary called kwargs.

# You can use any name you want for these as long as you know that one asterisk before the
# variable name (*) means positional arguments and two asterisks (**) means keyword arguments.
# The convention is to use *args and **kwargs, and that's what I will be using throughout this post.

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Getting familiar with *args and **kwargs

def args_func(*args):
    print(args)
    print(type(args))

args_func("abc", 123, "arrgh matey!", False, 4.19)

def kwargs_func(**kwargs):
    print(kwargs)
    print(type(kwargs))

kwargs_func(name="Matthew", age=25, likes_python=True, likes_snakes=False)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# You can still have other positional and keyword arguments in your function, but *args and **kwargs
# will handle all of the positional and keyword arguments after any others that are specified.

def func(arg1, arg2, *args, **kwargs):
    print(arg1)
    print(arg2)
    print(args)
    print(kwargs)

func("I am arg1", "I am arg2", 123, "abc", True, name="Matthew", age=25)

# Notice how "I am arg1" and "I am arg2" are the first 2 arguments passed to func and therefore
# are assigned to arg1 and arg2. The rest of the arguments, because they are not specified in the function 
# definition, find themselves in either args or kwargs based on if they were passed in as positional or
# keyword arguments. 

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# *args and **kwargs come in handy when you don't know how many arguments are going to be passed to your function.

# This add function can take any number of positional arguments, and as long as they are numbers,
# will add them all together and print out the total sum.
def add(*args):
    total = 0
    for num in args:
        total += num
    print(total)

add(1, 0.25, 7, 9.75, 5, 12, 3)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def calculate(start_value=0, **kwargs):
    total = start_value
    if kwargs["multiply"]:
        total *= kwargs["multiply"]
    if kwargs["divide"]:
        total /= kwargs["divide"]
    if kwargs["add"]:
        total += kwargs["add"]
    if kwargs["subtract"]:
        total -= kwargs["subtract"]
    
    print(total)

calculate(10, add=3, multiply=5, subtract=6, divide=4)

# As you can see, this function can take in any combination of these keyword arguments,
# and if a specific keyword argument is passed, will perform the required calculation.

# Based on the order of operations in the calculate function and the keyword arguments given, this does:
# 10 * 5 = 50
# 50 / 4 = 12.5
# 12.5 + 3 = 15.5
# 15.5 - 6 = 9.5

# Not a super useful function, but hopefully it gets the point across.

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# *args and **kwargs can also be useful in class init functions where you may not have all of
# the information upon initialization.

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.year = kwargs.get("year")
        self.miles = kwargs.get("miles")
        self.color = kwargs.get("color")

car = Car(make="Jeep", model="Wrangler", color="gray")
print(car.make, car.model, car.year, car.miles, car.color)
