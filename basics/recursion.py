
def calc_no_of_digits(num):
    if num / 10 == 0:
        return 1

    return 1 + calc_no_of_digits(num / 10)


num_of_digits = calc_no_of_digits(12342)

print("No of digits in 12342: " + str(num_of_digits))
