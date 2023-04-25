
phone_book = {}

print(phone_book)

phone_book = {
    "Vijaya Manohar Dogiparthi": +31645842,
    "VMD": +919739717537,
    "VMD": +919538848502,
}

print(phone_book["VMD"])

new_phone = {'Mr. ' + name: mobile for (name, mobile) in phone_book.items()}
print(new_phone)

del phone_book["VMD"]
print(phone_book)
