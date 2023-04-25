###########################################################

# def print_num(no_of_nums):
#     x = 0
#     while x <= no_of_nums:
#         print(str(x))
#         x += 1
# 
# print(print_num(10))

###########################################################
# Fill in the blanks to make the print_prime_factors function print 
# all the prime factors of a number. A prime factor is a number that
# is prime and divides another without a remainder.

# def print_prime_factors(number):
#       # Start with two, which is the first prime
#   factor = 2
#   # Keep going until the factor is larger than the number
#   while factor <= number:
#     # Check if factor is a divisor of number
#     if number % factor == 0:
#       # If it is, print it and divide the original number
#       print(factor)
#       number /= factor
#     else:
#       # If it's not, increment the factor by one
#       factor += 1
#   return "Done"
# 
# print_prime_factors(100)
# Should print 2,2,5,5

###########################################################
# The following code can lead to an infinite loop. Fix the code so that it can finish successfully for all numbers.

# Note: Try running your function with the number 0 as the input, and see what you get!

# def is_power_of_two(n):
#       if n == 0:
#     return False
# 
#   # Check if the number can be divided by two without a remainder
#   while n % 2 == 0:
#     n = n / 2
#   # If after dividing by two the number is 1, it's a power of two
#   if n == 1:
#     return True
#   return False
#   
# 
# print(is_power_of_two(0)) # Should be False
# print(is_power_of_two(1)) # Should be True
# print(is_power_of_two(8)) # Should be True
# print(is_power_of_two(9)) # Should be False

###########################################################

#def sum_divisors(n):
#    divisor = 2
#    sum_of_divisors = 1
#    
#    while divisor < n:
#        if n % divisor == 0:
#            sum_of_divisors += divisor
#            
#        divisor += 1    
#    
#    # Return the sum of all divisors of n, not including n
#    return sum_of_divisors
#
#print(sum_divisors(6)) # Should be 1+2+3=6
#print(sum_divisors(12)) # Should be 1+2+3+4+6=16

###########################################################

for x in range(10):
    print(x)

friends = ["Gullu", "George", "Davinci"]
for friend in friends:
    print(friend)


