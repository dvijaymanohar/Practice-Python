
"""
# The format_address function separates out parts of the address string into new strings:
# house_number and street_name, and returns: "house number X on street named Y".
#
# The format of the input string is: numeric house number, followed by the street name which may contain numbers,
# but never by themselves, and could be several words long.
#
# For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive".

def format_address(address_string):
    # house_number = []
    # street_name = []
    # address = address_string.split()
    # house_number = address[0]
    # street_name = address[1:]
    # print(house_number)
    # print(street_name)
    # return

    street_name = ""

    # Separate the address string into parts
    address = address_string.split()

    # Traverse through the address parts
    for x in address:
        # Determine if the address part is the
        # house number or part of the street name
        if x.isnumeric():
            house_number = int(x)
            # print(house_number)
        else:
            street_name += x
            street_name += " "

    # Remove the space at the end of the street name string
    street_name = street_name[:len(street_name) - 1]

    # Return the formatted string
    return "house number {} on street named {}".format(house_number, street_name)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"

"""

# The highlight_word function changes the given word in a sentence to its upper-case version.
# For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day".
# Can you write this function in just one line?

def highlight_word(sentence, word):
    if not word in sentence:
        print("word is not part of the given sentence")
        return

    # Get the list of words from the sentence
    words = sentence.split()

    pos = 0
    for x in words:
        # if not x.isalpha():
        #     print("{} is not alphabetic".format(x))
        #     continue

        for i in word:
            for j in x:
                if word[i] == x[j]:
                    continue
                else:
                    break

        if i == len(word):
            print("Word found")

        pos += 1

        # if x == word:
        #     print(x)
        #     break
        # pos += 1

    # words[pos] = words[pos].upper();

    return(words)

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))

