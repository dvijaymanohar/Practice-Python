

# Dynamic loading

class Animal:
    """Empty Doc String """

    def __init__(self):
        pass

    def print_animal(self):
        """Empty Doc String """
        print("Animal class ")

    def print_animal_two(self):
        """Empty Doc String """
        print("Animal class two functions: ")

# Lion class


class Lion(Animal):
    """Empty Doc String """

    def __init__(self):
        super()

    def print_animal(self):
        print("Lion class")


lion = Lion()

lion.print_animal()
lion.print_animal_two()
