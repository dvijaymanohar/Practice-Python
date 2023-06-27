



def practice_set_data_types():
    fruit_set = {'Apple', 'Banana', 'Orange'}
    if "Perziek" not in fruit_set:
        print("Perziek is not in the set")
    return

def practice_dictionary_data_type():
    family_mem_age = {"Vijay Manohar" : 40, "Divya" : 36, "Aaradhya": 8, "Siddhartha" : 5}
    family_mem_age["Vijay Manohar"] = 41
    print(family_mem_age)
    return


def practice_string_data_type():
    name = "Vijay Manohar"
    print("Name : {}".format(name))

    print("Character at index 5 is {}".format(name[6]))

    # name[5] = '_' # Strings in Python are immutable

    print("Name : {}".format(name))

def practice_list_data_type():
    fruits_list = ['Guvava', 'Banana', 'Apple']
    fruits_list.append('Perziek')
    print(fruits_list[2])
    fruits_list.remove('Perziek')
    print(fruits_list)
    return

def practice_tuple_data_type():
    fruits_tuple = ('Guvava', 'Banana', 'Apple')
    print(fruits_tuple[2])
    # fruits_tuple[1] = 'Apple' # Tuples in Python are immutable
    return


def practice_sequence_data_types():
    # practice_string_data_type()
    # practice_list_data_type()
    # practice_tuple_data_type
    practice_dictionary_data_type()

    return

def practice_int_data_types():
    num = int(input("Enter a number: "))
    print("Number : {}".format(num))

    num = 5.3
    print("Number : {}".format(num))

    num = 'a'
    print("Number : {}".format(num))
    return


if __name__ == "__main__":
    # practice_int_data_types()
    practice_sequence_data_types()