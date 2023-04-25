
import random

secret_num = random.randint(0, 100)

user_num = int(input('Enter the guessed number here: '))

no_of_allowed_chances = 0

while no_of_allowed_chances < 5:
    no_of_allowed_chances += 1

    if user_num > secret_num:
        print('Your chosen number is bigger, try again')
    elif user_num < secret_num:
        print('Your chosen number is smaller, try again')
    elif user_num == secret_num:
        print('You chose the correct number')
        break

    user_num = int(input('Enter the guessed number here: '))

if no_of_allowed_chances >= 5:
    print('You exhausted all the trails. Secret number is ' + str(secret_num))
