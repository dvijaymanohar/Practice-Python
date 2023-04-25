
"""
# The highlight_word function changes the given word in a sentence to its upper-case version.
# For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day".
# Can you write this function in just one line?

def highlight_word(sentence, word):
    if word not in sentence:
        print("word is not part of the given sentence")
        return

    # Get the list of words from the sentence
    words = sentence.split()

    # print(words)
    
    # print("Position: {}".format(sentence.index(word)))
    
    # for index, word in enumerate(words):
    #    print(index, word)
    
    # Position of a word in the list
    # print(words.index(word))
    
    pos = 0
    for x in words:
        if word in x:
            break
        pos += 1
    
    words[pos] = words[pos].upper();
    
    str = ""
    for x in words:
        str += x + " "
        # str += " "
    str = str[:len(str) - 1]
    
    return(str)

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))

"""

"""
##############
# A professor with two assistants, Jamie and Drew, wants an attendance list of the students, 
# in the order that they arrived in the classroom. Drew was the first one to note which students
# arrived, and then Jamie took over. After the class, they each entered their lists into the
# computer and emailed them to the professor, who needs to combine them into one, in the order
# of each student's arrival. Jamie emailed a follow-up, saying that her list is in reverse order.
# Complete the steps to combine them into one list as follows: the contents of Drew's list,
# followed by Jamie's list in reverse order, to get an accurate list of the students as they arrived.

def combine_lists(list1, list2):
    list = []
    
    for x in list2:
        list.append(x)
    
    no_of_elements_list1 = len(list1)
    
    for y in range((no_of_elements_list1 - 1), -1, -1):
        list.append(list1[y])
    
    return list
	
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))
"""

"""
###########
host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
print(host_addresses.keys())
"""

"""
##############
# List Comprehension

def squares(start, end):
    return [x *x for x in range(start, end + 1)]

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

"""

"""
##########
# Navigating to the dictionary contents

def car_listing(car_prices):
    result = ""
    
    for model, price in car_prices.items():
        result += "{} costs {} dollars".format(model, price) + "\n"
    
    return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

"""

"""
######
# Taylor and Rory are hosting a party. They sent out invitations, and each one collected responses into dictionaries,
# with names of their friends and how many guests each friend is bringing. Each dictionary is a partial list, but
# Rory's list has more current information about the number of guests. Fill in the blanks to combine both dictionaries
# into one, with each friend listed only once, and the number of guests from Rory's dictionary taking precedence,
# if a name is included in both dictionaries. Then print the resulting dictionary.

def combine_guests(guests1, guests2):
    dict = {}
    
    for guest1 in guests1.keys():
        dict[guest1] = guests1[guest1]
    
    # print(dict)
    
    # Combine both dictionaries into one, with each key listed 
    # only once, and the value from guests1 taking precedence
    for guest2 in guests2.keys():
        if guest2 not in dict.keys():
            dict[guest2] = guests2[guest2]
    
    return dict
    
Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))

"""

# Use a dictionary to count the frequency of letters in the input string. Only letters should be counted,
# not blank spaces, numbers, or punctuation. Upper case should be considered the same as lower case. 
# 
# For example, count_letters("This is a sentence.") should return {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.

def count_letters(text):
    result = {}
    
    # Go through each letter in the text
    for letter in text:
        # Check if the letter needs to be counted or not
        # Add or increment the value in the dictionary
        if letter.isalpha():
            letter = letter.lower()
            if letter in result.keys():
                result[letter] += 1
            else:
                result[letter] = 1
            
    return result

print(count_letters("!AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}