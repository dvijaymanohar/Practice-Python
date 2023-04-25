
formatter = "%r, %r, %r, %s"

print formatter % (1, 2, 3, 4)
print formatter % ("One^", "Two", "Three", "Four")
print formatter % (True, False, True, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I love the way, those hummers ride",
    "There are lots of interesting stories about Hummer Bikes",
    "Paratroopers jumping out of the planes with bikes.",
    'Montague Miltary standards'
)
