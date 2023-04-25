
from sys import argv

script, filename = argv

txt = open(filename)

print "Here is your file: %s\n" % filename
print txt.read()

txt.close();

print "Enter the another file name",
filename = raw_input()

print "Here is the filename: %s" % filename

txt = open(filename)

print txt.read()

txt.close();