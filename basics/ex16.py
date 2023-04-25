
from sys import argv

script, filename = argv

print "We are going to erase the file: %s" % filename
print "If you don't want to erase, press Ctrl + C.",
print "Otherwise, hit the Enter key."

raw_input("?")

file_obj = open(filename, 'w')
file_obj.truncate()

print "Enter three lines"

line = raw_input("Line #1:")
file_obj.write(line)
file_obj.write('\n')

line = raw_input("Line #2:")
file_obj.write(line)
file_obj.write('\n')

line = raw_input("Line #3:")
file_obj.write(line)
file_obj.write('\n')

file_obj.close()
