# Dunder/Magic Methods and the Python Data Model

# The way that Python's data model works, according Python's documentation, is
# that "all data in Python is represented by objects or by relations between objects".
# Every object has an "identity" and an identity is composed of a type and a value.

# An object's type can be thought of as the object's memory address and does not change
# once an object is created. An object's type also determines what values that object can have 
# and what operations you can perform on that object.

# All of that to say that everything in Python is represented by objects and those objects can only
# hold values and do the things that the object definition says they can.

# For example, a simple list is a Python object. You can check for yourself using, the code below:

a_list = [1, 2, 3]
print(type(a_list)) # <class 'list'>

# Because a list is an object, it has access to all of the operations that Python has defined for lists,
# like multiplication, getting the length, finding the index of an element within the list, etc. This concept is pretty cool
# and very powerful, because it means that we can implement the same kind of behavior in our own objects or even modify the
# behavior of existing objects.

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Dunder method is a short hand way to say "double underscore" method because all of these special methods take the 
# form of: def __method_name__(): where the method definition has two underscores before and after its name.
# You might also see these refereced as magic methods or just data model methods.

# Let's check out an example:

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

my_car = Car("Jeep", "Wrangler")

# Now that we have created a class and an instance of that class. What do you think happens when we try 
# to print our object?

print(my_car) # <__main__.Car object at 0x105113370>

# As of this line, we see that Python prints out the file name, object type, and memory address. 
# This is the default behavior and the information Python thinks we might find useful. This
# is not very valuable to us. We can change this however, using a special dunder method called __repr__. 
# What __repr__ does, is it allows us to "compute the 'official' string representation of an object", so that anytime
# we print it, it will show a string to represent the object. The best practice for creating a representation of
# an object is to try and make the representation a valid Python expression that you could use to recreate the object.
# Basically, if possible, the representation should look just like the line you used to create the object originally.

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def __repr__(self):
        return f"Car('{self.make}', '{self.model}')"

my_car = Car("Jeep", "Wrangler")

print(my_car) # Car('Jeep', 'Wrangler')

# Now we see that the value printed to the console looks like just the line of code we used to create the object, 
# and is much more readable and useful to us.

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# The below example might seem strange, but I think it's a good testament to the power of dunder methods
# and the degree to which we can customize the behavior of objects in Python.

# What do you think will happen if we try to multiply our car object by 2? Would it create
# another car object? Would it double the values of its attributes?

print(my_car * 2)

# If we try to run this now, Python will return: TypeError: unsupported operand type(s) for *: 'Car' and 'int'.
# So we see that we get an error. What if we want to be able to multiply our object by a number though?
# For this, we can again use a dunder method. In this case we would use the __mul__ method.

# What the __mul__ method does is it defines what Python should do when the * operator
# is used on an object. We can customize the operator to do whatever we want, but as an example, I will have it
# multiply the Car object's make and model attributes by the number following the * operator. 

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def __mul__(self, x):
        # It is important to note that Python doesn't know what you don't tell it, so if you try to multiply the object by
        # say, a string, you will get an error, and your method should probably handle these types of edge cases.
        if type(x) is not int:
            raise TypeError("Invalid argument. Must multiply Car by an int.")
        
        self.make = self.make * x
        self.model = self.model * x


my_car = Car("Jeep", "Wrangler")
print(my_car.make, my_car.model) # Jeep Wrangler

my_car * 2
print(my_car.make, my_car.model) # JeepJeep WranglerWrangler

my_car * "2" # TypeError

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# I'll leave you with one more example.
# Say we want to modify what happens when we call our object. We can do this with the __call__ dunder method.

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def __call__(self):
        print(f"You have called a {self.make} {self.model}")


my_car = Car("Jeep", "Wrangler")
my_car() # You have called a Jeep Wrangler


# Hopefully by this point, you have a better understanding of how Python works under the hood and can really see the power of dunder methods. 
# They essentially allow us to give our Python objects whatever functionality we want. The options are endless and the customization is very powerful.

# For a more in-depth explanation of Python's data model and a list of all of the available
# dunder methods, you can check out the documentation here: https://docs.python.org/3/reference/datamodel.html
