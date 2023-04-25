

class Coffee:
    # Constructor
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def check_budget(self, budget):
        # Check if the budget is valid
        if not isinstance(budget, (int, float)):
            print('Enter a valid number')
            exit()

        if budget < 0:
            print('Sorry, you don\'t have money')
            exit()

    def sell(self, budget):
        self.check_budget(budget)

        if self.name == 'small':
            if budget < self.price:
                print('Sorry, you cannot buy coffee!!')

        if budget >= self.price:
            print(f'You can buy the {self.name} coffee')

            if budget == self.price:
                print('Transaction done')
            else:
                print('Take the coffee and the change amount is ',
                      budget - self.price)

            exit('Thanks for your transaction')


small = Coffee('small', 10)
medium = Coffee('medium', 20)
big = Coffee('big', 30)

# print(id(small))
# print(type(small))
#
# if isinstance(medium, (Coffee)):
#     print('Medium is the instance of the class Coffee')

try:
    user_budget = float(input('Enter your budget: '))
except ValueError:
    exit('Enter a valid number')

for coffee in [big, medium, small]:
    coffee.sell(user_budget)
