

guess_number = 25

while True:
    number = input("Guess the number: ")

    try:
        number = int(number)
    except:
        print('Sorry, that is not a number')
        continue

    if number != guess_number:
        if number > guess_number:
            print('Given number is greater than the guess_number. Try again')
        elif number < guess_number:
            if guess_number % number == 0:
                print(
                    'Given number is smaller than the guess_number and also a multiple of the secret number. Try again!!')
            else:
                print('Given number is smaller than the guess_number. Try again')
    else:
        print('You guessed the correct number. Congratulations!!')
        break
