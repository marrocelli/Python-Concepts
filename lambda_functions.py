# Lambda Functions

# Lambda functions, also called anonymous functions, are simple functions that can be used to evaluate a single expression. 
# For a simple, single-expression function, you will often times not want to write out a whole function definition for it.
# This is where lamda functions are useful. Within a lambda function, you can do anything that you would do with a regular function with the exception
# that your return value must be a single expression. This means that you can pass multiple parameters, including optional 
# parameters to a lambda function (see optional_parameters.py file for more info on these).

# Below you will learn about the anatomy of lambda functions, how to use them, and some examples of common use-cases.

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Your code before learning about lambda functions

def add_five(x):
    return x + 5

print(add_five(2)) # 7

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Anatomy of a lamda function:

# lambda parameter(s): expression

# First you specify the lambda keyword followed by a comma separated list of any parameters the lambda function will take.
# After the function parameters you will add a colon followed by the expression that you want to be evaluated.

# If you find yourself wanting to use a lambda function multiple times throughout your program, 
# because a lambda function is an expression, you can use a variable to represent it.
add_five = lambda x: x+5

print(add_five(9)) # 14

# To apply a lambda function to an argument in a single line you can wrap the lambda function in parenthesis and follow
# with the argument you want to apply it to also wrapped in parenthesis.
x = (lambda x: x+5)(7)
print(x) # 12

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Lambda functions with multiple parameters, including optional parameters

add = lambda x, y=3: x+y
print(add(7)) # 10

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Lambda functions with map() and filter()

# Lambda functions are also very useful when used with the map and filter functions.
# (see map_and_filter_functions.py file for more info on these.)

# Instead of creating a function that will only be used once within the map or filter function,
# we can use a lambda function to handle everything on one line.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map() with lambda function
doubled_nums = map(lambda num: num * 2, nums)
print(list(doubled_nums)) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# filter() with lambda function
odd_nums = filter(lambda num: num % 2 != 0, nums)
print(list(odd_nums)) # [1, 3, 5, 7, 9]
