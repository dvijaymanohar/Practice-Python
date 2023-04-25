
n = int(input("Enter the no. of numbres here: "))

total_sum = 0

for num in range(n):
    number = float(input("Enter the number here: "))
    total_sum += number

print('Average of the given numbers: ' + str(total_sum / n))
