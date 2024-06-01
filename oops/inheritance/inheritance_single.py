

class Vehicle:
    """ Vehicle descriptor """
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def get_brand(self):
        return self.brand, self.model

# Single inheritance
class FuelCar(Vehicle):
    " This class models the FuelCar "
    def __init__(self, brand, model, fuel_type):
        self.fuel_type = fuel_type
        Vehicle.__init__(self, brand, model)

    " This function gets the details of the car "
    def get_details(self):
        print('Car brand: ', self.brand)
        print(f'Model : {self.model}')
        # print(f'Fuel Type: {self.fuel_type}')
        print("Fuel type: ".format(self.fuel_type))


car_type = FuelCar('Volkswagen', 'Polo', 'Petrol')
brand, model = car_type.get_brand()

print('Car brand: ', brand)
print(f'Car model : {model}')

car_type.get_details()

car_type.price = 10000

print(car_type.price, car_type.model)

# Delete the create object C1
# del car_type

print(car_type.__doc__)
