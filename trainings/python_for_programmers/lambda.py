
# def num(num): return num * 10
#
#
# def tripple(num): return num ** 3 if num > 0 else -1
#
#
# crazy = lambda str1, str2, str3 : str1[0] + str2[0] + str3[0] if len(str1) != 0 and len(str2) != 0 and len(str3) != 0 else "Crazy"
#
#
# print("Calling lambda: ", num(10))
# print("Tripple lambda: ", tripple(-10))
# print("Checking crazy stuff: ", crazy('VMD', 'Vijay', ''))

def calculator(operation, num1, num2):
    return operation(num1, num2)


addition = calculator(lambda num1, num2: num1 + num2, 10, 20)
subtraction = calculator(lambda num1, num2: num1 - num2, 10, 20)

print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")


numList = [1, 2, 3, 4, 5, 'VMD']

# intList = list(map(lambda num: num ** 2 if isinstance(num, (int)) else 0, numList))


def foo(num):
    retVal = 0

    if isinstance(num, (int)):
        retVal = num ** 2
    else:
        retVal = 0

    return retVal

# Make a list that takes only the integers from the given list
# intList = list(map(foo, numList))
# print(intList)

# Remove 0s from the list
print(list(filter(lambda num: num != 0, list(map(foo, numList)))))


