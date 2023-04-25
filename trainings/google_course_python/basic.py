
#########################
# Example 1

# my_variable = 10
#
# print(my_variable)
#
# my_string_var = "Vijay"
#
# print(my_string_var)

#######################
# Hello World

# my_variable = "Hello World"
# my_variable = my_variable
# val = 10
# 
# print(my_variable)
# 
# my_variable = val
# 
# my_variable += 1
# 
# my_var2 = my_variable
# 
# print(my_variable)
# print(my_var2)
# 
##############s#########

# Class Example

# class ExampleClass:
#     "This is a docstring. This is my first atempt to create a class in Python"
#     def foo(self):
#         print('Hello Foo')
#     
#     def boo(self):
#         print('Hello boo')
# 
# ob = ExampleClass()
# 
# ob.foo()
# 
# ob.boo()


# def is_positive(number):
#     if number > 0:
#         return True
#     else:
#         return False
# 
# positve_num = is_positive(-5)
# 
# print(positve_num)
# 
# print(2**2 == 4)

# If a filesystem has a block size of 4096 bytes, this means that a file comprised of 
# only one byte will still use 4096 bytes of storage. A file made up of 4097 bytes will
# use 4096*2=8192 bytes of storage. Knowing this, can you fill in the gaps in the 
# calculate_storage function below, which calculates the storage size needed for a given filesize?


# def calculate_storage(filesize):
#     block_size = 4096
#     # Use floor division to calculate how many blocks are fully occupied
#     full_blocks = filesize // block_size
#     # Use the modulo operator to check whether there's any remainder
#     partial_block_remainder = filesize % block_size
#     # Depending on whether there's a remainder or not, return the right number.
#     if partial_block_remainder > 0:
#         return (full_blocks + 1) * block_size
#     return full_blocks * block_size
# 
# print(calculate_storage(1))    # Should be 4096
# print(calculate_storage(4096)) # Should be 4096
# print(calculate_storage(4097)) # Should be 8192
# print(calculate_storage(6000)) # Should be 8192
# 
# def sum(x, y):
#     		return(x+y)
# print(sum(sum(1,2), sum(3,4)))
# 
# def color_translator(color):
#     if color == "red":
#         hex_color = "#ff0000"
#     elif color == "green":
#         hex_color = "#00ff00"
#     elif color == "blue":
#         hex_color = "#0000ff"
#     else:
#         hex_color = "unknown"
#     return hex_color
# 
# print(color_translator("blue")) # Should be #0000ff
# print(color_translator("yellow")) # Should be unknown
# print(color_translator("red")) # Should be #ff0000
# print(color_translator("black")) # Should be unknown
# print(color_translator("green")) # Should be #00ff00
# print(color_translator("unknown")) # Should be unknown

###############################################################
#
# Complete the body of the format_name function. This function receives
#  the first_name and last_name parameters and then returns a properly formatted 
# string.
# 
# Specifically:
# 
# If both the last_name and the first_name parameters are supplied, the function 
# should return:
# 
# "Name: last_name, first_name"
# 
# If only one name parameter is supplied (either the first name or the last name),
# the function should return:
# 
# "Name: name"
# 
# Finally, if both names are blank, the function should return the empty string:

# def format_name(first_name, last_name):
#     if len(first_name) > 0 and len(last_name) > 0:
#         return "Name: " + last_name + ', ' + first_name
#     elif len(first_name) > 0 and len(last_name) == 0:
#         return "Name: " + first_name
#     elif len(first_name) == 0 and len(last_name) > 0:
#         return "Name: " + last_name
#     else:
#         return "\"\""
# 
# print(format_name("Ernest", "Hemingway"))
# # Should be "Name: Hemingway, Ernest"
# 
# print(format_name("", "Madonna"))
# # Should be "Name: Madonna"
# 
# print(format_name("Voltaire", ""))
# # Should be "Name: Voltaire"
# 
# print(format_name("", ""))
# # Should be ""

####################################################################################3
# The longest_word function is used to compare 3 words. It should return the word with
# the most number of characters (and the first in the list when they have the same length).
# Fill in the blank to make this happen.


# def longest_word(word1, word2, word3):
#     if len(word1) >= len(word2) and len(word1) >= len(word3):
#         word = word1
#     elif len(word2) >= len(word1) and len(word2) >= len(word3):
#         word = word2
#     elif len(word3) >= len(word1) and len(word3) >= len(word2):
#         word = word3
#     else:
#         word = word1
#     return(word)
# 
# print(longest_word("chair", "couch", "table"))
# print(longest_word("bed", "bath", "beyond"))
# print(longest_word("laptop", "notebook", "desktop"))
# print(longest_word("laptop", "laptop", "laptop"))
# print(longest_word("chair", "couch", "cup"))

"""

###############################################################
# The fractional_part function divides the numerator by the denominator, and returns
# just the fractional part (a number between 0 and 1). Complete the body of the
# function so that it returns the right number. Note: Since division by 0 produces an
# error, if the denominator is 0, the function should return 0 instead of attempting
# the division.

def fractional_part(numerator, denominator):
    # Operate with numerator and denominator to 
    # keep just the fractional part of the quotient
    if denominator == 0:
        val = 0
    else:
        val = (numerator / denominator) % 1
    return val

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0


def format_name(first_name, last_name):
    if len(first_name) > 0 and len(last_name) > 0:
        return "Name: " + last_name + ', ' + first_name
    elif len(first_name) > 0 and len(last_name) == 0:
        return "Name: " + first_name
    elif len(first_name) == 0 and len(last_name) > 0:
        return "Name: " + last_name
    else:
        return "\"\""

print(format_name("Ernest", "Hemingway"))
# Should be "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should be "Name: Madonna"

print(format_name("Voltaire", ""))
# Should be "Name: Voltaire"

print(format_name("", ""))
# Should be ""

###########################################################3333
number = 1
while number <= 7:
    print(number, end=" ")
    number += 1

def show_letters(word):
    for i in word:
        print(i)

show_letters("Hello")

"""

# Count the no. of digits in a number
def digits(n):
    count = 0
    if n == 0:
        count = 1
    while (n > 0):
        count += 1
        n //= 10
        # print('n = ' + str(n))
    return count

def div(a, b):
    return a // b

# print(div(25, 5))

print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1
# Should print one line per letter