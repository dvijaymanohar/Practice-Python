
"""
# This function prints out a multiplication table (where each number is the result
# of multiplying the first number of its row by the number at the top of its column).
# Fill in the blanks so that calling multiplication_table(1, 3) will print out:

# 1 2 3
# 
# 2 4 6
# 
# 3 6 9

def multiplication_table(start, stop):
    for x in range(start, stop + 1):
        for y in range(start, stop + 1):
            print(str(x * y), end = " ")
        print()

multiplication_table(1, 3)
# Should print the multiplication table shown above

"""

"""
def votes(params):
    for vote in params:
        print("Possible option:" + vote)

# print(votes(['Yes', 'No', 'May be']))

"""

"""
for x in range(10):
    for y in range(x):
        print(y)
"""

"""
for x in range(1, 10, 3):
    print(x)

"""

"""
def decade_counter():
    # year = 1
    while year < 50:
        year += 10
    return year

print(str(decade_counter()))

"""

"""
# The counter function counts down from start to stop when start is bigger than stop,
# and counts up from start to stop otherwise. Fill in the blanks to make this work correctly.

def counter(start, stop):
    x = start
    if start > stop:
        return_string = "Counting down: "
        while x >= stop:
            return_string += str(x)
            if x > stop:
                return_string += ","
            x -= 1
    else:
        return_string = "Counting up: "
        while x <= stop:
            return_string += str(x)
            if x != stop:
                return_string += ","
            x = x + 1
    return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"

"""

# The loop function is similar to range(), but handles the parameters somewhat differently: 
# it takes in 3 parameters: the starting point, the stopping point, and the increment step. When 
# the starting point is greater than the stopping point, it forces the steps to be negative. When,
# instead, the starting point is less than the stopping point, it forces the step to be positive. 
# Also, if the step is 0, it changes to 1 or -1. The result is returned as a one-line, space-separated string of numbers. 
# For example, loop(11,2,3) should return 11 8 5 and loop(1,5,0) should return 1 2 3 4. Fill in the missing parts to make that happen.


def loop(start, stop, step):
    return_string = ""
    if step == 0:
        if start > stop:
            step = -1
	if ___:
		step = abs(step) * -1
	else:
		step = abs(step)
	for ___:
		return_string += str(count) + " "
	return return_string.strip()

print(loop(11,2,3)) # Should be 11 8 5
print(loop(1,5,0)) # Should be 1 2 3 4
print(loop(-1,-2,0)) # Should be -1
print(loop(10,25,-2)) # Should be 10 12 14 16 18 20 22 24 
print(loop(1,1,1)) # Should be empty