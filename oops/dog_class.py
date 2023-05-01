
class Dog:
    AnimalType = "mammal"

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("My name is {}".format(self.name))


dog = Dog("Tomy")
dog.speak()
