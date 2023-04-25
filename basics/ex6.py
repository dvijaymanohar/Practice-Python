

x = "There are %d types of people" %10
binary = "binary"
do_not = "don't"
y = "There are %s people who know binary and %s" %(binary, do_not)

print x
print y

# Just print anything with the format specifier: %r
print "I said: %r %r times so far." %(x, 2)
print "I said: %s." %x

hilarious = True

# Embedding a format specifier in a string variable
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation
print joke_evaluation % hilarious

w = "This is the left side of ..."
e = " a string with a right side."

# String concatenation with overloaded + operator
print w + e
