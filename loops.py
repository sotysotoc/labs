import sys

# Lists in Python
# Lists are used to store multiple items in a single variable
fruits = ["apple", "banana", "cherry"]

# We can have multiple data types inside the list data structure
mixed_list = ["ananas", 1, True, 3.14]

# In Python, the 'for' loop is used for iterating over elements of a sequence.
# It can be used with lists, tuples, strings, dictionaries, and more.

for fruit in fruits:
    print(f"I like {fruit}!")


for character in "Ana are ananas":
    print(character)
    '''
    The output in this for loop
    A
    n
    a

    a
    r
    e

    a
    n
    a
    n
    a
    s
    '''

# While Loop
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1

# Range Function
# The range() function generates a sequence of numbers that can be used in loops.
# range(start, stop, step) 
# start and step are optional and by default start is 0 an step is 1

# Example: Generate numbers from 0 to 4
for i in range(5):
    print(i)

# You can specify a starting point, ending point, and step size.
# Example: Generate even numbers from 2 to 10
for i in range(2, 11, 2):
    print(i)

# Accessing Elements in a List
numbers = [1, 2, 3, 4, 5]

# Accessing elements by index
print(numbers[0])  # Prints the first element (1)

# Accessing the last element using negative index
print(numbers[-1])  # Prints the last element (5)

# List Operations
# Concatenating lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print(concatenated_list)  # Prints [1, 2, 3, 4, 5, 6]

# Multiplying a list
multiplied_list = list1 * 3
print(multiplied_list)  # Prints [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Example for why * would be useful for generating a list
print([0] * 10)

# Tuples
coordinates = (3, 4)
first_names = ('Simon', 'Sarah', 'Mehdi', 'Fatime')

# Accessing elements
print(coordinates[0])  # Prints the first element (3)

# You cannot modify a tuple's elements once it's created.
# coordinates[0] = 1 <- this expression throws an error

"""
Besides the intuitive difference between tuples and lists, as mentioned before, 
tuples are immutable, so unlike lists, tuples cannot be modified. 
However, some technical differences make tuples an undeniable asset in Python programming.
"""
a_list = ['abc', 'xyz', 123, 231, 13.31, 0.1312]
a_tuple = ('abc', 'xyz', 123, 231, 13.31, 0.1312)
print('The list size:', sys.getsizeof(a_list), 'bytes') #The list size: 104 bytes
print('The tuple size:', sys.getsizeof(a_tuple), 'bytes') #The tuple size: 88 bytes

# List Comprehensions
# List comprehensions provide a concise way to create lists.
# General syntax:
# new_list = [expression for variable in sequence]

# Example: Create a list of squares of numbers from 1 to 5
squares = [x**2 for x in range(1, 6)]
print(squares)  # Prints [1, 4, 9, 16, 25]

# Using loops and conditionals in list comprehensions
even_squares = [x**2 for x in range(1, 6) if x % 2 == 0]
print(even_squares)  # Prints [4, 16]
