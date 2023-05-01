import sys

batman = "Vijaya Manohar"
print(batman[len(batman) -1])
print(batman[-1])
print(batman[-9])

print(batman[0:4])

print(batman[1:-1:3])

print(len(batman))
print(batman[13:0:-1])
print(batman[::2])
print(batman[::-1])
print(batman[13:0])

print(batman[::-1])
print(batman[13::-1])

print(type(4 / 2))

print((12.4 // 2), type(12.4 // 2))

print(-28 % 10)

print(id(batman))

batman2 = batman
print(id(batman2))

if batman is batman2:
    print("Both are reffering to the same object")