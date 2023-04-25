

def factorial(num):

    if num < 0:
        print('Factorial of negative numbers is not computed')
        return -1

    factorial = 1

    while num > 0:
        factorial *= num
        num -= 1

    print('Factorial func: Identifier of the given number: ', id(num))
    print(locals())
    print(globals())

    return factorial


def mul_by_num(listNum, num):
    length = len(listNum)

    for x in range(length):
        listNum[x] *= num


if __name__ == '__main__':
    num = input('Enter the num to find the factorial: ')

    try:
        num = int(num)
    except ValueError:
        exit('Enter a valid interger')

    print('Main: Identifier of the given number: ', id(num))
    print(factorial(num))
    print(num)

    listNum = [1, 2, 3, 4, 5]
    mul_by_num(listNum, 10)

    print(listNum)
