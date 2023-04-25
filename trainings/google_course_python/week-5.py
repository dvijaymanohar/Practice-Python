
"""
list = []
dict = {}
tup = ()

print(type(list))
print(type(dict))
print(type(tup))
print(type(""))

print(dir(""))
print(help(""))

"""

"""
#############

class Apple:
      color = ""
      flavour = ""

Marriegold = Apple()

Marriegold.color = "red"
Marriegold.flavour = "sweet"

print(Marriegold.flavour)
"""

"""
#######
class Flower:
      color = 'unknown'

rose = Flower()
rose.color ="red"

violet = Flower()
violet.color = "blue"

this_pun_is_for_you = Flower()

print("Roses are {},".format(rose.color))
print("violets are {},".format(violet.color))
print(this_pun_is_for_you) 
    
"""

"""
#######
class Piglet:
    name = "piglet"
    age = 0
    
    def speak(self):
        print("I am {}, Oink".format(self.name))

    def age_in_month(self):
        age_in_months = self.age * 12
        print("{} piggy is {} months old".format(self.name, age_in_months))
        return age_in_months

hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()

petunia = Piglet()
petunia.name = "Petunia"
petunia.speak()

petunia.age = 2
petunia.age_in_month()

"""

class Person:
    """ Describes the person class """
    
    name = ""
    
    def __init__(self, name):
        self.name = name

    def greetings(self):
        """ Says Greetings """
        return ("hi, my name is {}".format(self.name))
    
    def __str__(self):
        return ("Hi, this is {}".format(self.name))

# Create a new instance with a name of your choice
some_person = Person("Tammu")

# Call the greeting method
print(some_person.greetings())

print(some_person)

help(some_person.greetings)