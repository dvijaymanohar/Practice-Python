
# Below statement to avoid in case of an encoding error
# -- coding: utf-8--

name = "Vijay Manohar D."
age = 36
birth_year = 1983
height = 161 # cms
weight = 65.0 # kgs
eyes = 'black'
teeth = 'brown'
hair = 'bald'

print "Lets talk about Mr. {}" .format(name)
print "He's %d cms (%f inches) tall" % (height, height / 2.54)
print "He's %f kgs heavy" % weight
print "Actually he is heavy for his height"
print "He has %s eyes and %s hair" % (eyes, hair)
print "No of years happened after his birth: %d" % (2019 - birth_year)
#print "Rounded Value: %f" round(1.73338)


