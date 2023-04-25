

formatter = "%r %r %r %r"
print(formatter %(1, 2, 3, 4))

print(formatter %(True, False, True, True))
print(formatter % ('One', 'Two', 'Three', 'Four'))
print("%s %s %s %s" % ('One', 'Two', 'Three', 'Four'))
print(formatter % (
    "Jack and Jill",
    "Went up the hill",
    "To fetch a pail of water",
    'Jack fell down and broke his arm'
))