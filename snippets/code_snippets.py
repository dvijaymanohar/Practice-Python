
name = 'Vijaya Manohar Dogiparthi'

output = 'Vijay' if name == 'Vijaya Manohar Dogiparthi' else 'Vijay Manohar Dogiparthy'
print(output)


print(type('Unicode rocks 😎'))

# Creating a tuple and range
x = (1, 2, 3, 4)   # a tuple is an immutable sequence
y = x[3]           # assign the 4th element in the tuple to y
print(y)           # print the integer 4

x = range(1, 4)     # create a range from 1 (inclusive) to 4 (exclusive)
y = tuple(x)       # return a new tuple from the range
print(y)           # prints (1, 2, 3)

y[1] = 3           # y is immutable this will throw a TypeError exception


# List comprehension
doubles_list = [x * 2 for x in range(10)]
print(doubles_list)

# To know the type
print(type(doubles_list))

# to list all the functions supported by string
for item in dir(str):
    print(item)
