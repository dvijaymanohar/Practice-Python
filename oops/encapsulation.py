
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model


car = Car("Volkwagen", "Up")
print("Car make and model: " + str(car.get_make()) + " " + str(car.get_model()))
