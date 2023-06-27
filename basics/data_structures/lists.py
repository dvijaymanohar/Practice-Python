# List operations


def list_operations():
    fruit_list = []
    fruit_list.append('Banana')
    fruit_list.append('Orange')
    fruit_list.append('Apple')
    fruit_list.append('Mango')
    fruit_list.append('Pineapple')
    fruit_list.append('Strawberry')

    # Printing the whole list
    print(fruit_list)

    # Printing the first item in the list
    print(fruit_list[0])

    # Printing at a specific position
    print(fruit_list[1])

    # Printing the length of the list
    print(len(fruit_list))

    # Printing the last item in the list
    print(fruit_list[-1])

    # Printing all items in the list
    print(fruit_list[:])

    # Printing all items in the list except the last one
    print(fruit_list[:-1])

    # Printing all items in the list except the first one
    print(fruit_list[1:])

    # Printing all items in the list except the first and last one
    print(fruit_list[1:-1])

    # Printing all items in the list except the second and last one
    print(fruit_list[2:-2])

    fruit_list.sort()

    print(fruit_list)

    print("{} is the fruit at index 2".format(fruit_list.pop(2)))

    print(fruit_list)

    return



if __name__ == '__main__':
    list_operations()