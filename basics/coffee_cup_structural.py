

small = 10
medium = 20
big = 30

user_budget = input('Enter the amount user has:')

try:
    user_budget = int(user_budget)
except:
    print('Enter a valid number')
    exit()

if user_budget > 0:
    if user_budget >= big:
        print("You can afford a bigger cup of coffee.")
        if user_budget == big:
            print("Take the bigger cup of cofee. Transaction is completed!!")
        else:
            print('Take the bigger cup and the change amount: ',  user_budget - big)
    elif user_budget >= medium:
        print("You can afford a medium cup of coffee.")
        if user_budget == medium:
            print("Take the medium cup of cofee. Transaction is completed!!")
        else:
            print('Take the medium cup and the change amount: ',
                  user_budget - medium)
    elif user_budget >= small:
        print("You can small a medium cup of coffee.")
        if user_budget == small:
            print("Take the small cup of cofee. Transaction is completed!!")
        else:
            print('Take the small cup and the change amount: ',
                  user_budget - small)
    else:
        print('You can\'t get a cup of coffee. Work hard to find money!!')
else:
    print('Sorry, you don\'t have money. Work hard to find money!!')
