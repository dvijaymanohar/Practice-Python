
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s file to %s file\n" % (from_file, to_file)

#in_file = open(from_file, 'r')
#data = in_file.read()

data = open(from_file, 'r').read()

out_file = open(to_file, 'w')
out_file.write(data)

#in_file.close()
out_file.close()


