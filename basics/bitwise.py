
# Assigning a binary num
num = 0b100111

# Getting the length of the binary number
print(num.bit_length())

# Getting the decimal equivalent of the binary number
print(num)


def set_bit(num, position):
    mask = 1 << position

    print('Before:', bin(num))

    num |= mask

    print('After:', bin(num))

def toggle_bit(num, position):
    mask = 1 << position

    print('Before:', bin(num))

    num ^= mask

    print('After: ', bin(num))

    return num

num = 29

set_bit(num, 13)
toggle_bit(num, 5)

print(bin(29))

