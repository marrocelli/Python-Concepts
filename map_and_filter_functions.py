# map() and filter()

# What are they? 

# The map() function allows you to apply a function to every item in a list (or any other iterable data type)
# and then creates a new list with those new values.
# Map function is essentially doing the same thing as the for loop (verify this),
# but the map function is a useful short-cut. and a lot cleaner. Map function takes two parameters, a function and a list,
# and will apply that function to every element in the list.

# The filter() function allows you to filter items in a list through a function and if that
# function (for a given value from the list) returns True, it is added to the new list, if it returns
# False, that value will not be added to the list.
# Filter function also takes two parameters, a function and a list. 


# Map and filter functions can be very useful when combined and are often used together.

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# If asked to return all of the doubled values of a given list, before knowing 
# about the map function you might have solved the problem like so:
nums = [1, 2, 3, 4, 5]

def double(num):
    return num * 2

doubled_nums = []
for x in nums:
    doubled_nums.append(double(x))

print(doubled_nums) # [2, 4, 6, 8, 10]

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Map Function

# Using the map function, your solution might look something like this:
nums = [1, 2, 3, 4, 5]
doubled_nums = []

def double(num):
    return num * 2

doubled_nums = map(double, nums)
# Because map function doesn't return a list (returns a map object), must cast the object to a list data type.
print(list(doubled_nums))

# Because the map object is an iterable, you could also return the values using a for loop:
print(type(doubled_nums))
for num in doubled_nums:
    print(num)


# Another way to accomplish the same thing is through a list comprehension, but I will save that for a future post.
doubled_nums = [double(x) for x in nums]
print(doubled_nums)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Filter function

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_odd(x):
    return x % 2 != 0

# Filters the list nums through the is_odd function and returns all values of nums
# where is_odd evaluates to True, which will be all of the odd numbers.
odd_nums = filter(is_odd, nums)
print(list(odd_nums)) # [1, 3, 5, 7, 9]

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Another example for the filter function

names = ["Alex", "John", "Alice", "Matt", "Travis", "Arnold"]
def starts_with_a(name):
    return name[0] == "A"

a_names = filter(starts_with_a, names)
print(list(a_names))

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Combining map and filter

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_odd(x):
    return x % 2 != 0

def add_7(x):
    return x + 7

odd_nums = filter(is_odd, nums)
odd_nums_plus_seven = map(add_7, odd_nums)
print(list(odd_nums_plus_seven)) # [8, 10, 12, 14, 16]

# could also save a line with: 
odd_nums_plus_seven = map(add_7, filter(is_odd, nums))

print(list(odd_nums_plus_seven)) # [8, 10, 12, 14, 16]
