
num = "01011"


def do_job(num):
    no_of_iterations = 0

    while num != 0:
        if num % 2 == 0:
            num /= 2
        else:
            num -= 1

        no_of_iterations += 1

    return no_of_iterations


if __name__ == '__main__':
    try:
        num = int(num, 2)
    except ValueError:
        print('Invalid number')

    print(f'Given number : {num}')

    print(f'No. of iterations: {do_job(num)}')

num = 5
print(num)

num = "VMD"
print(num)