
import sys
print(3 * 'ha')

name = 'Vijaya Manohar Dogiparthi'

print('Vijay' in name)


print(type(name))
print('Memory occupied by the variable name: ', sys.getsizeof(name))
print('lenght of the string name: ', len(name))

print('Unique identifier of the string: ', id(name))
# print('dir of the string name: ', dir(name))


my_string = "0123456789"
print(my_string[-2: 4: -1])

output = "Vijay" if name == 'Vijaya Manohar Dogiparthi' else "Vijay Manohar Dogiparthy"
print(output)


# ===
random_string = "Thcis fdgd vis a string"
print(random_string.find("is"))  # First instance of 'is' occurs at index 2
print(random_string.find("is", 9, 13))  # No instance of 'is' in this range

# ==
# print(ord('₹'))
# print(ord('♚'))
#
# print(str(12) + '.453')
# print(str(True))
# print(str(123.4) + ' is a string')
#
# print(bool(10.3))
# print(hex(344))
# print(complex(4, 3))
#
# print(float('453'))
# print(float(True))


def rep_cat(x, y):
    try:
        x = str(x)
        y = str(y)
    except:
        return ''

    return 10 * x + 5 * y


print(rep_cat(3, 4))
