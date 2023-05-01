
class ComplexNumber:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def display(self):
        print(self.real,  "+",  self.imag, 'j')

    def __add__(self, c):
        result = ComplexNumber()
        result.real = self.real + c.real
        result.imag = self.imag + c.imag

        return result


c1 = ComplexNumber(5, 10)
c2 = ComplexNumber(5, 15)

c3 = ComplexNumber()

c3 = c1 + c2

c3.display()
