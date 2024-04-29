

def divide(x, y):
    """
    Practice for raising the exception if the division by zero is attempted

    Parameters:
    x, y: x/y

    Returns:
    Division value

    """

    if y == 0:
        raise Exception("Division by zero is not allowed")

    return x / y


try:
    x = int(input("Enter the number for numerator: "))
    y = int(input("Enter the number for denominator: "))

    ret = divide(x, y)

except ZeroDivisionError as e:
    print(e)
else:
    print(f"The result is {ret}")
finally:
    print("Done")
