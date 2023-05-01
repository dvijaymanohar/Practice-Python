
from os import execlp


def fininacii_series(n):
    n1 = 0
    n2 = 1
    counter = 2

    while counter < n:
        if n1 == 0:
            print("%d\t%d\t" % (n1, n2), end='')
            continue

        print("%d\t" % (n1 + n2), end='')

        n1 = n2

        n2 += n1

        counter += 1


if __name__ == "__main__":
    num = input("Enter the number:")
    try:
        num = int(num)
    except:
        print("Enter a valid number")
        exit()

    fininacii_series(num)
