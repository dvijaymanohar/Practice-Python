


# for x in range(10):
#     print(x)
# 
# friends = ["Gullu", "George", "Davinci"]
# for friend in friends:
#     print(friend)
# 

# values = [3, 5, 23, 78, 23, 78, 34]
# length = 0
# sum = 0
# for value in values:
#     sum += value
#     length += 1
# 
# print("sum of numbers is " + str(sum))
# print("Average of numbers is " + str(sum / length))

##
# product = 1
# for i in range(1, 10):
#     product *= i
# 
# print(product)

########################################################
# Factorial of a number

# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
# 
# print(factorial(4)) # should return 24
# print(factorial(5)) # should return 120

########################################################

# Farenhiet temparature to celsius
#def to_celsius(x):
#    return (x - 32) * 5 / 9
#
#
#for i in range(0, 101, 10):
#    print(i, to_celsius(i))
#
########################################################

# Dominos

# for left in range(7):
#     for right in range(left, 7):
#         print('[' + str(left) + ',' + str(right) + ']', end = " ")
#     print()    

# Basket ball team
# for left in range(7):
#     for right in range(left + 1, 7):
#         print('[' + str(left) + ',' + str(right) + ']', end = " ")
#     print()    

########################################################

# teams = ['Dragons', 'Pandas', 'Unicorns', 'Gorillas', 'Wolves']
# 
# for home_team in teams:
#     for away_team in teams:
#         if home_team != away_team:
#             print(home_team + ' vs ' + away_team)

########################################################
# for x in [25, 26]:
#     print(x)

# def greet_friends(friends):
#     for x in friends:
#         print("Hi " + x)
# 
# greet_friends(["Vijay", "Aaradhya", "Tammu", "Mummis"])
# 
# def validate_users(users):
#     for user in users:
#         if len(user) >= 3:
#             print(user + " is valid")
#         else:
#             print(user + " is invalid")
# 
# validate_users(["purplecat"])
  
########################################################
  
# for x in range(100):
#     if x %7 == 0:
#         print(x)
        
########################################################

def factorial_n(n):
    if n < 2:
        return n
    
    return n * factorial_n(n - 1)

# print("Factorial of a number: " + str(factorial_n(1000)))

"""
########################################################
def is_power_of(number, base):
    if number == 1:
        # If number is equal to 1, it's a power (base**0).
        return True
    
    # Base case: when number is smaller than base.
    if number < base:
        return False

    # Recursive case: keep dividing number by base.
    return is_power_of(number / base, base)

print(is_power_of(8, 2)) # Should be True
print(is_power_of(64, 4)) # Should be True
print(is_power_of(70, 10)) # Should be False
print(is_power_of(9, 3)) # Should be True
print(is_power_of(9, 4)) # Should be True

"""

# The loop function is similar to range(), but handles the parameters somewhat differently: 
# it takes in 3 parameters: the starting point, the stopping point, and the increment step.
# When the starting point is greater than the stopping point, it forces the steps to be negative.
# When, instead, the starting point is less than the stopping point, it forces the step to be positive.
# Also, if the step is 0, it changes to 1 or -1. The result is returned as a one-line, space-separated 
# string of numbers. For example, loop(11,2,3) should return 11 8 5 and loop(1,5,0) should return
# 1 2 3 4. Fill in the missing parts to make that happen.

############################################################
def loop(start, stop, step):
    return_string = ""
    
    if step == 0:
        step = -1
    if start > stop:
        step = abs(step) * -1
    else:
        step = abs(step)
  
    for count in range(start, stop, step):
        return_string += str(count) + " "
 
    return return_string.strip()

print(loop(11,2,3)) # Should be 11 8 5
print(loop(1,5,0)) # Should be 1 2 3 4
print(loop(-1,-2,0)) # Should be -1
print(loop(10,25,-2)) # Should be 10 12 14 16 18 20 22 24 
print(loop(1,1,1)) # Should be empty

