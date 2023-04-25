
"""
fruit = "Pineapple"
print(fruit[4])
print(fruit[-1])
print(fruit[:4])
print(fruit[4:])
print(fruit[:7])
print(fruit[:15])
print(fruit[3:7])

"""

"""
message = "london bridge is falling down"
# message[0] = 'L'
new_message = 'L' + message[1:]
print(message)
print(new_message)

message = "London bridge is falling down, falling down"
print(message)

"""


"""
pets = "Cats and Dogs"

# Check whether one string contains in an another string
val = "Cats" in pets
print(val)

print(pets.index("and"))
print(5)

"""

"""
print("Vijay Manohar Dogiparthi".split())
pets = "Cats and Dogs"

print(str(pets[0]))

"""

"""
vmd_name = "Vijaya Manohar Dogiparthi"
divya_name = "Divya Nagabandi"
aushy_name = "Aaradhya Dogiparthi"
sid_name = "Siddhartha Dogiparthi"

str_len = len(vmd_name) * 5

print("Hi {}, your lucky number is {}".format(vmd_name, str_len))

print("Hi {name}, string length of your name is {length}".format(length=len(vmd_name), name=vmd_name))
print("Hi {name}, string length of your name is {length}".format(length=len(divya_name), name=divya_name))
print("Hi {name}, string length of your name is {length}".format(length=len(aushy_name), name=aushy_name))
print("Hi {name}, string length of your name is {length}".format(length=len(sid_name), name=sid_name))

"""

"""
def student_grade(name, grade):
    return "{} received {}% on the exam".format(name, grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

"""

"""
price_of_the_item = 10
value_added_tax = 14 * 10 / 100

print("Total price of the item: ${:.2f}".format(price_of_the_item + value_added_tax))

"""


"""
def to_celsius(x):
    return (x - 32) * 5 / 9

for x in range(1, 100, 10):
    print("{:>3} F | {:>6.3f} C".format(x, to_celsius(x)))

"""

"""
name = "Vijay"

for i in name:
    print(i)

"""  

"""
############ 
# Question 2
# The permissions of a file in a Linux system are split into three sets of three permissions: read, write,
# and execute for the owner, group, and others. Each of the three values can be expressed as an octal number
# summing each permission, with 4 corresponding to read, 2 to write, and 1 to execute. Or it can be written 
# with a string using the letters r, w, and x or - when the permission is not granted. For example: 640 is 
# read/write for the owner, read for the group, and no permissions for the others; converted to a string, 
# it would be: "rw-r-----" 755 is read/write/execute for the owner, and read/execute for group and others;
# converted to a string, it would be: "rwxr-xr-x" Fill in the blanks to make the code convert a permission
# in octal format into a string format.

def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for x in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if x >= value:
                result += letter
                x -= value
            else:
                result += "-"
    return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------

"""

###########
# Let's create a function that turns text into pig latin: a simple text transformation that modifies
# each word moving the first character to the end and appending "ay" to the end. For example, python
# ends up as ythonpay.

def convert_text_to_list(text):
    return text.split()

def pig_latin(text):
    say = ""
    
    # Separate the text into words
    words = convert_text_to_list(text)
    
    for word in words:
        # Create the pig latin word and add it to the list
        say += word[1:] + word[0] + "ay "
        # Turn the list back into a phrase
    return say
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

