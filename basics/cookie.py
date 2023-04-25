

class Cookie:
    def __init__(self, name, shape, flavor='Choclate'):
        self.name = name
        self.shape = shape
        self.flavor = flavor

    def bake(self):
        print(f'Cookie is baked with the {self.shape} shape and {self.flavor} flavor')
        print('Enjoy your cookie')


if __name__ == '__main__':
    c1 = Cookie('Awsome Cookie', 'Diamond', 'Vanila')
    c1.bake()
