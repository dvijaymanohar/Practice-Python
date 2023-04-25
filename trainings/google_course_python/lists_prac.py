
"""

x = ["Ausshy", "started", "managing", "the", "family", "photographs", "since", "1st", "of", "March", "2020!!"]

print(x[4])
print(len(x))

print("Tammu" in x)

print(x[2:5])

"""

"""
# The group_list function accepts a group name and a list of members, and returns a string with the
# format: group_name: member1, member2, … For example, group_list("g", ["a","b","c"]) returns "g: a, b, c". Fill in the gaps in this function to do that.

def group_list(group, users):
    members = ""
    for x in users:
         members += x
         members += ", "
    members = members[:len(members) - 2]
    return group + ": " + members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"

"""

"""
def find_emp_no(employee_name, employee_num_list, employee_num):
    if employee_num > len(employee_num_list):
        return "Give employee number is out of range"
  
    for x in range(len(employee_num_list)):
        if x == employee_num:
            return employee_name[employee_num] + ": " + str(employee_num)
    
    return "Given employee record was not found"
    
employees = ["Vijaya Manohar Dogiparthi", "Divya Nagabandi", "Aaradhya Dogiparthi", "Siddhartha Dogiparthi"]
employee_num_list = [1, 2, 3, 4]

print(find_emp_no(employees, employee_num_list, 0))
print(find_emp_no(employees, employee_num_list, 1))
print(find_emp_no(employees, employee_num_list, 2))
print(find_emp_no(employees, employee_num_list, 3))
print(find_emp_no(employees, employee_num_list, 4))

"""
#####################

"""
def skip_elements(elements):
    fruits = []
    
    for x in range(len(elements)):
        if not(x % 2):
            fruits.append(elements[x])
            
    return fruits

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

fruits = ["Apple", "Banana", "Pear", "Peach", "Grapes"]
print(fruits)
    
"""
##############

"""
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = (seconds - minutes * 60 - hours * 3600)
    
    return hours, minutes, remaining_seconds

time = convert_seconds(8976)
print(type(time))

print(convert_seconds(7537))

hours, minutes, seconds = time
print(hours, minutes, seconds)
print(time)
"""


"""
###################
# The guest_list function reads in a list of tuples with the name, age, and profession of each party guest,
# and prints the sentence "Guest is X years old and works as __." for each one. For example, 
# guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) should print out:
# 
# Ken is 30 years old and works as Chef.
# 
# Pat is 35 years old and works as Lawyer.
# 
# Amanda is 25 years old and works as Engineer.
# 
# Fill in the gaps in this function to do that.

def guest_list(guests):
    for guest in guests:
        print("{} is {} years old and works as {}".format(guest[0], guest[1], guest[2]))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

"""

"""
################
animals = ["Zebra", "Monkey", "Donkey", "Octopus", "Lion", "Tiger"]

chars = 0

for animal in animals:
    chars += len(animal)
   
print("No. of characters: {}, Average length of each item: {}".format(chars, chars/len(animals)))

"""

"""
# Try out the enumerate function for yourself in this quick exercise. Complete the skip_elements
# function to return every other element from the list, this time using the enumerate function to
# check if an element is on an even position or an odd position.

def skip_elements(elements):
    tup = []
    for index, element in enumerate(elements):
        if not(index % 2):
            tup.append(element)
    return tup

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

"""

"""
###################3
# Iterating over Lists and Tuples

def full_email(members):
    result = []
    
    for name, email in members:
        result.append("{} <{}>".format(name, email))
        
    return result

print(full_email([("Vijay Manohar Dogiparthi", "dvijaymanohar@gmail.com"),
       ("Divya Nagabandi", "drdivyanagabandi@gmail.com")]))

"""

"""
############
# Multiples
# Multiples = []
# 
# for i in range(1, 11):
#     Multiples.append(7 * i)
#     
# print(Multiples)

def multiple_table(num):
    Multiples = [x * num for x in range(1, 11)]
    return Multiples 
    
print(multiple_table(5))

"""

"""
##########
# List Comprehensions

Languages = ["C", "C++", "Python", "Bash Scripting"]
lengths = [len(language) for language in Languages]

print(lengths)

def get_even_data(some_list):
    even_list = [some_list[x] for x in range(len(some_list)) if x % 2 == 0]
    return even_list

print(get_even_data(["a", "e", "f", "g", "f", "f", "j"]))

"""

"""
############
# Given a list of filenames, we want to rename all the files with the extension hpp to
# the extension h by generating a list of tuples of the form (old_name, new_name).

# That is, given the following list of filenames
# 
# filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# 
# complete the starter code to generate the following newfilenames list of tuples
# 
# newfilenames = [('program.c',  'program.c'),
#                  ('stdio.hpp',  'stdio.h'), 
#                  ('sample.hpp', 'sample.h'),
#                  ('a.out',      'a.out'),
#                  ('math.hpp',   'math.h'),
#                  ('hpp.out',    'hpp.out')]

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames = []

def new_file_extn(file_name):
    filename = file_name.split(".")
    return filename[0] + ".h"

def get_file_extn(file_name):
    filename = file_name.split(".")
    return filename[1]

for filename in filenames:
    extn = get_file_extn(filename)

    if extn == "hpp":
        newfilenames.append((filename, new_file_extn(filename)))
    else:
        newfilenames.append((filename, filename))
    
print(newfilenames)
# Should be [('program.c', 'program.c'),
#            ('stdio.hpp', 'stdio.h'), 
#            ('sample.hpp', 'sample.h'),
#            ('a.out', 'a.out'),
#            ('math.hpp', 'math.h'),
#            ('hpp.out', 'hpp.out')]

"""

####
def conv_sentence_to_list(sentence):
    return sentence.split()

sentence = "Vijaya Manohar Dogiparthi"
print(conv_sentence_to_list(sentence))