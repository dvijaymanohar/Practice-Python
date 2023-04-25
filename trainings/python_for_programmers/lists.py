
# random_list = [1, 2.3, 'VM Dogiparthi', True]
# print('My name is ', random_list[2])
# print('Total length of the list: ', len(random_list))


# num_seq = range(0, 11, 1)
# num_list = list(num_seq)
# print('Num sequence: ', num_list)


# world_cup_winners = [[2006, "Italy"], [2010, "Spain"],
#                      [2014, "Germany"], [2018, "France"]]
#
# print(world_cup_winners[0][0])

# part_A = [1, 2, 3, 4, 5]
# part_B = [6, 7, 8, 9, 10, 'VMD']
# merged_list = part_A + part_B
# print(merged_list)


# list_1 = []
# list_1.append(1)
# list_1.append(2)
# list_1.append(3)
# print(list_1)

# num_list 1= [1, 2, 3, 3, 5, 6]
# num_list.insert(3, 4)  # Inserting 4 at the 3rd index. 5 and 6 shifted ahead
# print(num_list)
#
# num_list.insert(18, 7)  # Inserting 4 at the 3rd index. 5 and 6 shifted ahead
# print(num_list)
#
# num_list.pop()
# print(num_list)
#
# num_list.remove(13)
# print(num_list)


# ===
# List slicing

# num_list = [1, 2, 3, 4, 5, 6, 7, 8]
#
# print(num_list[2:5])
# print(num_list[0::2])

# ==
# Index of the given element

# cities = ["London", "Paris", "Los Angeles", "Beirut"]
# print(cities.index("Los Angeles"))  # It is at the 2nd index

# ==
# List Comprehension

# nums = [10, 20, 30, 40]
# nums_double = []
#
# # for n in nums:
# #     nums_double.append(n * 2)
#
# # nums_double = [n * 2 for n in nums]
# nums_double = [n * 2 for n in nums if n % 3 == 0]
#
# print(nums_double)

# ==

# Mixing of two lists

num1 = [1, 4, 7, 3, 879, 3, 67]
num2 = [56, 8, 3, 9, 45, 890]

print([(n1, n2) for n1 in num1 for n2 in num2 if n1 + n2 > 10])
print([num1, num2])

if 56 in num2:
    print('Its there')


