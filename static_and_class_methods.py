# Static and Class Methods

# What are they?

# Class Methods
# Class methods are functions that are bound to a class itself rather than an instance of a class. 
# Because of this, a class method can be called on any instance of a class or even on the class itself.
# You don't actually need to have an object of a class already created to use one of its class methods.
# Class methods are created with the built-in @classmethod decorator. Class methods do not take a self
# parameter, but will take at least one parameter. You can name this parameter whatever you want, but
# in the example code below, I use cls to represent the class object that is implicitly passed to the method. 
# Class methods have access to and can modify any class variables, which would apply those changes across 
# all instances of that class. Another use for class methods are to create factory methods (similar to construtors)
# which create and return new class objects. 

# Static Methods
# Static methods are similar to class methods, but don't take a self or class parameter. Because of this,
# static methods can't access or modify class variables like a class method can. Static methods are created with
# the built-in @staticmethod decorator. Static methods behave much like a regular function, and only have access 
# to the variables that are passed to it. The key difference being that static methods are called from a class or
# instance of that class. At this point, you might be wondering what is the point of a static method then?
# Static methods, although they don't provide any additional functionality to your programs, are a good way to
# organize your methods if their functionality has some logical connection to the class you put them in. Static methods
# are more of an organizational tool/stylistic choice than anything, but will come in handy and make your code
# much cleaner when utilized correctly.

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

from datetime import date

class Person:

    # CLASS VARIABLES
    species = "Homo Sapien"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def get_species(cls):
        """
        Get the value of the class variable "species".
        :return: str
        """
        return cls.species

    @classmethod
    def create_person_from_birth_year(cls, name, year):
        """
        Factory method that create a new instance of the Person class given a birth year.
        :param name: str
        :param year: int
        :return: Person
        """
        return cls(name, date.today().year - year)
    
    @staticmethod
    def is_adult(age):
        """
        Given an age, returns a boolean for if that person is an adult.
        :param age: int
        :return: boolean
        """
        return age >= 18
    
    def display(self):
        """ Prints information about a person. """
        print(f"{self.name} is {self.age} years old.")


# class method call
species = Person.get_species()
print(species)

# class method call
new_person = Person.create_person_from_birth_year("Matthew", 1996)

new_person.display()

# static method call
print(Person.is_adult(16))
