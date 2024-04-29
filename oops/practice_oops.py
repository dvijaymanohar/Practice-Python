
# """_
# summary_
# """
#
#
# class Test:
#     """
#     This class represents a simple class
#     """
#     count = 0
#
#     def __init__(self):
#         self.count += 1
#
#
# # test.count = 0
#
# obj1 = Test()
# obj2 = Test()
# obj3 = Test()
#
# print(Test.count)
# print(obj1.count)


##

# """
# _summary_
# """
#
#
# class Dog:
#     """
#         Dog class
#     """
#     def __init__(self, name=None, bread=None):
#         self.name = name
#         self.bread = bread
#
#     def bark(self):
#         """_summary_
#         """
#         print(f"{self.name} says woof!")
#
#
# obj1 = Dog("Scooby", "Long lived one")
# obj1.bark()

##

# """
#     Inheritance
# """
#
#
# class Animal:
#     """
#       Animal class
#     """
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         """
#             What animal speaks
#         """
#         print(f'{self.name} makes a sound')
#
#
# class Dog(Animal):
#     def speak(self):
#         """
#             Dog speak
#         """
#
#         print(f'{self.name} says woof!')
#
#
# d = Dog("Puppy")
# d.speak()


##

# """
#     Encapsulation
# """
#
#
# class Encapsulation:
#     """
#         Demonstrates encapsulation
#     """
#
#     def __init__(self, balance):
#         self._balance = balance
#
#     def deposit(self, amount):
#         self._balance += amount
#
#     def withdraw(self, amount):
#         if amount > self._balance:
#             print('Insufficient funds')
#         else:
#             self._balance -= amount
#
#
# obj = Encapsulation(10)
# obj.deposit(10)
# obj.withdraw(30)


##

# # Exception handling
#
# class CustomException(Exception):
#     """_summary_
#
#     Args:
#         Exception (_type_): _description_
#     """
#     pass
#
#
# def divide(a, b):
#     """_summary_
#
#     Args:
#         a (_type_): _description_
#         b (_type_): _description_
#
#     Raises:
#         CustomException: _description_
#
#     Returns:
#         _type_: _description_
#     """
#     if b == 0:
#         raise ZeroDivisionError
#         raise CustomException('Cannot divide by zero')
#     return a // b
#
#
# try:
#     res = divide(1, 2)
#     print(f'Result: {res}')
#
#     res = divide(1, 0)
#     print(f'Result: {res}')
#
# except CustomException as e:
#     print(e)
# except ZeroDivisionError:
#     print("Division by zero attempt foiled")
#

##

# class Vector2D:
#     """
#     Vector class
#     """
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return Vector2D(self.x + other.x, self.y + other.y)
#
#     def __str__(self):
#         return f'{self.x} + i{self.y}'
#
#
# vec1 = Vector2D(3, 5)
# vec2 = Vector2D(6, 7)
# vec3 = vec1 + vec2
#
# print(vec3)


###
#
# def calc(*args):
#    total = 0
#
#    for arg in args:
#        total += arg
#
#    return total
#
#
# print(f'Addition: {calc(1, 2, 3, 4)}')


class Circle:
    def __init__(self, radius):
        # Note the underscore convention for private variables
        self._rad = radius

    @property
    def radius(self):
        return self._rad

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._rad = value

    @radius.deleter
    def rad(self):
        del self._rad


# Usage
c = Circle(5)
print(c.rad)  # Accessing the property
c.rad = 10  # Setting the property
print(c.rad)
del c.rad  # Deleting the property
