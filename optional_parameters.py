# Optional Parameters

# What are they?
# Optional parameters are exactly what their name says they are: parameters that are optional. To go a little deeper, optional parameters
# are parameters that when not given an explicit value in a function call, will be given a default value specified in the function defintion.

# Reasons why you would want to use optional parameters?
# If you find yourself passing in the same arguments to a function repeatedly, you could set some optional parameters that will default to
# the values you use most often to avoid tediously typing out all of the parameters, which will also make your code easier read. 
# Especially in the case of initializing object attributes, you may not know what the attributes are yet when initialize the object, so 
# you may not want to set a value yet and just take a default in the meantime.
# You don't always know what parameters/how many parameters will be passed in. A function may do very different things depending on 
# what/how many arguments are passed in. Optional parameters give your functions more flexibility.

# Problems you could run into if not done correctly:
# for example if you do not give a default value in function defintion and you don't pass in a value
# in a function call, you will get something like -> TypeError: func() missing 1 required positional argument: "x"

# Notes:
# Default value will only be used if a value is not passed to the variable in the function call. Otherwise, the value you passed to the 
# function call will override the default value.


# To make a parameter optional, just put an "=" and a default value in the function definition.
# If no value for an optional parameter is given in a function call, it will be assigned the default value.

# If no arguments are given to the function double, num will default to 1 and the function will return 2.
def double(num=1):
    return num * 2

x = double(6)
print(x)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# In this example, frequency is optional with a default value of 1.
def repeat_words(word, frequency=1):
    return (word * frequency)

words = repeat_words("Python", 5)
print(words)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

class Car:
    # condition and mileage are optional parameters.
    def __init__(self, make, model, year, condition="New", mileage="0"):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.mileage = mileage
    
    # show_all is an optional parameter
    def display_info(self, show_all=True):
        if show_all:
            print(f"{self.condition} {self.year} {self.make} {self.model} with {self.mileage} miles.")
        else:
            print(f"{self.year} {self.make} {self.model}")

car = Car("Jeep", "Wrangler", 2013, "Used", 100000)
car.display() # show_all will take the default value
car.display(show_all=False)


