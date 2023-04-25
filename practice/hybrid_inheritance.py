

class Vehicle:
    """ vehicle"""

    def __init__(self, reg_code, manufacturer, model):
        print("Vehicle Parameterised constructor called")
        self.reg_code = reg_code
        self.manufacturer = manufacturer
        self.model = model

    def get_details(self):
        """ get details of vehicle """
        print("Registration Code: ", self.reg_code)
        print("Manufacturer: ", self.manufacturer)
        print("Model: ", self.model)

# Single inheritance
# FuelCar extending Vehicle class


class FuelCar (Vehicle):
    """ ef"""

    def __init__(self, reg_code, manufacturer, model, fuel_type):
        print("FuelCar parameterised constructor called")
        self.fuel_type = fuel_type
        Vehicle.__init__(self, reg_code, manufacturer, model)

    def get_details(self):
        """ get details of FuelCar """
        print("Fuel Type: ", self.fuel_type)


class ElectricCar(Vehicle):
    """ ElectronCar class """

    def __init__(self, reg_code, manufacturer, model, is_li_battery):
        print("ElectricCar parameterised constructor called")
        self.is_li_battery = is_li_battery
        Vehicle.__init__(self, reg_code, manufacturer, model)

    def get_details(self):
        """ get_details """
        print("Electric Type: ", self.is_li_battery)


class HybridCar(FuelCar, ElectricCar):
    """ ef"""

    def __init__(self, reg_code, manufacturer, model, fuel_type, is_li_battery,
                 tank_capacity, battery_capacity):
        print("HybridCar parameterised constructor called")
        self.tank_capacity = tank_capacity
        self.battery_capacity = battery_capacity
        FuelCar.__init__(self, reg_code, manufacturer, model, fuel_type)
        ElectricCar.__init__(self, reg_code, manufacturer,
                             model, is_li_battery)

    def get_details(self):

        # print("Registration Code: ", self.reg_code)
        # print("Manufacturer :", self.manufacturer)

        print("Electric Type: ", self.tank_capacity)


def main():
    """ main """
    hybrid = HybridCar("TP650H", "Volswagen", "Up",
                       "Gasolene", True, 40.00, 100)
    hybrid.get_details()


main()
