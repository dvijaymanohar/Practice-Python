
def square_num_range(end_num):
    for num in range(1, end_num):
        print(num ** 2)

def check_prime(n):
    prime_num = True

    if n == 2 or n == 3: return True

    for factor in range(2, n - 1):
        if n % factor == 0:
            prime_num = False
            break
    return prime_num


if __name__ == '__main__':
    print("Enter the number here: ")
    n = int(input())

    if check_prime(n):
        print("{} is a prime number".format(n))
    else:
        print("{} is not a prime number".format(n))

    print("Enter the number here: ")
    n = int(input())
    square_num_range(n)
