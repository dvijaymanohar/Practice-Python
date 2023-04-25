from sys import argv

script, username = argv

prompt = '\"\"'

print "Hi %s, I'am the script %s" %(username, script)
print "I'd like to ask you few questions."
print "Do you like me %s?" % username
likes = raw_input(prompt)

print "Where do you live, %s?" % username
lives = raw_input(prompt)

print "Mr. %s, What kind of computer do you have?" % username
computer = raw_input(prompt)

print """
    Dear Mr. %s,

        Do you like Python: %s.
        You are put up at %s.
        You have a computer: %s.
        Nice.
""" % (username, likes, lives, computer)


