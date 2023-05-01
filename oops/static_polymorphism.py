
"""Empty Doc String """


class SumNum:
    """Empty Doc String """

    def __init__(self):
        """Empty Doc String """
        pass

    def sum_num(self, a_var, b_var, c_var=0):
        """Empty Doc String """
        return a_var + b_var + c_var


Obj = SumNum()
print("Sum of 1, 3 is ", Obj.sum_num(1, 3))
print("Sum of 1, 2, 3 is ", Obj.sum_num(1, 2, 3))
