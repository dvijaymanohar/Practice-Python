
# from __future__ import division


def div(num):
    for i in range(num):
        print(i)

        x = float(i) / 49

        print(x, type(x))

        if float(x) == 0:
            break

        i += 50


float_list = [2.5, 16.42, 10.77, 8.3, 34.21]

for x in float_list:
    x *= 2


def double_at_even_places(float_list):
    print(float_list)

    for i in range(0, len(float_list)):  # Iterator traverses to the last index of the list
        if i % 2 != 0:
            pass

        float_list[i] = float_list[i] * 2

    print(float_list)


n = 50
num_list = [10, 4, 23, 6, 18, 27, 47]


def find_sum_equalto(num_list):
    for n1 in num_list:
        found = False

        for n2 in num_list:
            if n1 + n2 == n:
                found = True
                break

        if found == True:
            print(f'Pair: {n1, n2}')
            break


def pow(num, exponent):
    pow_value = 1

    if not (isinstance(num, int) and isinstance(exponent, int)):
        print('Invalid inputs')
        return -1

    if exponent == 0:
        return 1

    if num == 0:
        return 0

    while exponent > 0:
        pow_value *= num
        exponent -= 1

    return pow_value


#x = input('Enter the number here: ')
#
# try:
#    x = int(x)
# except ValueError:
#    exit('Enter a valid number')

# print(pow(x, 10))


def sum_of_first_and_last_digits(num):
    if num < 10:
        return num

    last_digit = num % 10

    print('last digit', last_digit)

    while num > 10:
        num = num // 10

    return num + last_digit


# print(f'{sum_of_first_and_last_digits(x)}')


def check_balance(brackets):
    if not isinstance(brackets, (str)):
        print('Invalid input')

    if len(brackets) == 0:
        return True

    opens = 0
    closed = 0

    for x in range(len(brackets)):
        if brackets[x] == '[':
            opens += 1
            continue

        if brackets[x] == ']':
            closed += 1

    if opens == closed:
        return True
    else:
        return False


# print(f'{check_balance("[[[[][]]]]")}')

def check_sum(num_list):
    if len(num_list) == 0 or len(num_list) == 1:
        return False

    for x in range(len(num_list)):
        for y in range(x + 1, len(num_list)):
            if num_list[x] + num_list[y] == 0:
                return True

    return False

# print(f'{check_sum([10, -14, 26, 5, -3, 13, -5])}')
# print(f'{check_sum([10, -14, 26, 5, -3])}')


def fib(n):
    if n < 0:
        return -1

    first = 0
    second = 1

    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        for x in range(n - 2):
            third = first + second
            first = second
            second = third

    return third


print(f'{fib(7)}')
print(f'{fib(-1)}')
