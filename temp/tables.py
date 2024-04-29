"""
Module Name

A brief description of the module and its purpose.

Author: Vijaya Manohar Dogiparthi
Date: Date of creation or last modification

"""


def print_nth_table(n: int) -> None:
    """
        Prints the nth multiplication table.

        Parameters:
        n (int): the number of rows in the multiplication table

        Returns:
        None

    """
    for i in range(1, 11):
        print(f'{i} * {n} = {i * n}')


# if __name__ == "main":
print_nth_table(9)
