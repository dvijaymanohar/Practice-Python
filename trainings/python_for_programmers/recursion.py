

def print_num(num):
    if num != 0:
        print_num(num - 1)

    print(f'{num}, ')


# Print 0 to n numbers using recursion
# print_num(100)


def factorial(num):
    if num == 0 or num == 1:
        return 1
    elif num < 0:
        return -1

    return num * factorial(num - 1)


# Client code
# num = input('Enter the number to know its factorial here: ')
#
# try:
#     # num = isinstance(num, (int))
#     num = int(num)
# except:
#     exit('Enter a valid integer')
#
# if num > 0:
#     print(f'Factorial of {num} is {factorial(num)}')

def fib(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(6))
