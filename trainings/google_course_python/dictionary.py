"""

dict = {'name1':"Vijay Manohar Dogiparthy", 'name2':"Divya Nagabandi", 'name3':"Aaradhya Dogiparthi", 'name4':"Siddhartha Dogiparthi"}
print(dict)
print(dict.get("name4"))
print(dict["name1"])

result = "name1" in dict
print(result)

result = "name5" in dict
print(result)

dict["Quality1"] = "Growth Mindset"
print(dict)

dict["Quality1"] = "Work hard"
print(dict)

print("name7" in dict)

del dict["Quality1"]
print(dict)

"""

"""
###############
file_counts = {"jpg":10, "py":15, "c":2000, "h":150}

for extension in file_counts:
    print(extension)

for ext, num in file_counts.items():
    print("There are {} files with .{} extension".format(num, ext))


print(file_counts.keys())

print(file_counts.values())

"""

"""
###############
# odd squares
odd_squares = {x: x * x for x in range(11) if (x % 2)}
even_squares = {x: x * x for x in range(11) if x % 2 == 0}

print(odd_squares)
print(even_squares)

print(2 not in odd_squares)
print(2 in even_squares)

"""

"""
## Count letters in the given text
def count_letters(text):
    dict = {}
    for letter in text:
        if letter not in dict:
            dict[letter] = 0
        dict[letter] += 1
    return dict

# print(count_letters("A journey of 1000 miles start with a single step"))

"""

"""
##############
wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}

# for x in wardrobe.keys():
#     print(x)
# 
# for y in wardrobe.items():
#     print(y)  
 
for x in wardrobe.keys():
    for i in wardrobe[x]:
        print("{} {}".format(i, x))

print(wardrobe.values())

"""

"""
##########
# The email_list function receives a dictionary, which contains domain names as keys, and a list
# of users as values. Fill in the blanks to generate a list that contains complete email addresses
# (e.g. diana.prince@gmail.com).


def email_list(domains):
    emails = []
    
    for domain in domains.keys():
        for user in domains[domain]:
            emails.append("{}@{}".format(user, domain))
    
    return emails

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], 
                  "yahoo.com": ["barbara.gordon", "jean.grey"],
                   "hotmail.com": ["bruce.wayne"]}))

"""


# The groups_per_user function receives a dictionary, which contains group names with the list of users.
# Users can belong to multiple groups. Fill in the blanks to return a dictionary with the users as keys
# and a list of their groups as values.

def groups_per_user(group_dictionary):
    user_groups = {}

    # Go through group_dictionary
    for group in group_dictionary.keys():
        # print(group)
        # Now go through the users in the group
        
        for user in group_dictionary[group]:
        # Now add the group to the the list of
        # groups for this user, creating the entry
        # in the dictionary if necessary
            user_groups.setdefault(user, []).append(group) 

    return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))
