
# Cat Class
class CatClass:
    " This is the Cat Class for practice of OOPs with Python"
    ColorOfCat = 'Black'
    
    " This function gets the color of the cat"
    def GetColorOfCat(self):
        " Color of the cat function"
        # print("Color of the cat: " + ColorOfCat)
        print("Color of the cat: " + self.ColorOfCat)
        print('\n')
    
    pass

# Client Code
obj = CatClass()

obj.GetColorOfCat()
print(obj.__doc__)




