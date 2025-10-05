# Lab 06 Jana Johnson in CS 1400
# Tuesday, September 23, 2025
# 12:55 PM

# GOALS
# Explore properties of Lists
# Work with loops and function in the context of lists



# 1. Making a list ----------------------------------------------------------------
# Create a list variable called simple_list with values ("Hello", 4, 6.77) in that order.

simple_list = ["Hello", 4, 6.77]


# 2. List index ----------------------------------------------------------------
# List indexes start at 0; the first element: 1; the second element: 2, etc.
# Accessing an index can be done with square brackets []

# An expression to get the *last value* in the simple_list.
#print(simple_list[2])

# Access the fist element with a negative index.
#print(simple_list[-1])
# access the fist element with a negative index.

# Replace the value at index 2 with the string "Goodbye"
simple_list[2] = "Goodbye"
#print(simple_list)

# Add an element to the end of the list
simple_list.append("Goodbye")



# Delete elements from lists  ----------------------------------------------------------------

#   (1) remove() method ----------
#   removes a specific element
# simple_list.remove()

#   (2) .pop() method ----------
#   removes a specific index
simple_list.pop(0)

#   (3) del keyword ----------
#   removes a specific index
del simple_list[0]


def letter_list(word):
    new_list = []
    for letter in word:
        new_list.append(letter)
    return new_list

print(letter_list("Hello"))

