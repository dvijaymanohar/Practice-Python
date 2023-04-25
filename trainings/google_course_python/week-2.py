
# print('a' + 'b' + 'c')

# file_sizes = 4 + 5 + 6 + 7
# average = file_sizes / 4
# print("The average filesize : " + str(average))

def convert_secs(seconds):
    hours = seconds // 3600
    minutes = (seconds - (hours * 3600)) // 60
    seconds = (seconds - (hours * 3600) - (minutes * 60))
    return hours, minutes, seconds

hours, minutes, seconds = convert_secs(10000)

print(str(hours) + ' : ' + str(minutes) + ' : ' + str(seconds))