

def add_to_nums(a, b):
    return a + b

if __name__ == "main":
    x = int(input("Enter the first number here: "))
    y = int(input("Enter the second number here: "))
    print("Sum of {} and {} number is {}", format(x, y, add_to_nums(x, y)))
