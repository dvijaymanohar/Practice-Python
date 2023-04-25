
class ComplexNumber:
    "Class for the Complex Number"
    def __init__(self, r = 0, i = 0):
        self.real = r
        self.imag = i
        print('Constructor of the complex number called\n')

    def getdata(self):
        print("{0} + {1}j".format(self.real, self.imag))


# Create a ComplexNumber object
C1 = ComplexNumber(2, 3)

C2 = ComplexNumber(4, 5)
C2.newVar = 11

C1.getdata()
C2.getdata()

print(C2.real, C2.imag, C2.newVar)

# Deleting the attribute in an object
del C2.newVar

# print(C2.real, C2.imag, C2.newVar)

# Delete the create object C1
del C1

# Delete the create object C1
del C2

print(C2.real, C2.imag, C2.newVar)
