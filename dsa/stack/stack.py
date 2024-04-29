
"""
This stack class supports push, pop, peek and is_empty methods

"""


class Stack():

    """
    A class representing the stack datastructure.

    This class provides a simple implementation of a stack datastructure.
    It includes methods for common stack operations

    Attributes:
        push(item): Push the the item onto the stack
        pop(item): Pop the item off the stack
        is_empty(): True if the stack is empty
        peek(): Returns the top of the stack
        get_stack(): Returns the top of the stack
    """

    def __init__(self):
        """
        Initialize the stack

        """
        self.items = []

    def push(self, item):
        """Push the the item onto the stack

        Args:
            item (integer): Item to push onto the stack
        """
        self.items.append(item)

        return 0, 0  # Success: return result and status code 0

    def pop(self):
        """Pop the item off the stack

        Returns:
            Item on the top of the stack
        """
        if len(self.items) != 0:
            result = self.items.pop()
            status = 0
        else:
            result = None
            status = 1

        return result, status

    def is_empty(self):
        """Check if the stack is empty
        """
        result = len(self.items) == 0

        return result, 0

    def peek(self):
        """Returns the top element on the stack
        """
        result = self.items[-1]

        return result, 0

    def get_stack(self):
        """Returns the complete list that makes up the stack
        """
        result = self.items

        return result, 0


# obj = Stack()

# print(f"Is stack empty: {obj.is_empty()}")

# obj.push(5)

# for i in range(0, 10):
#     obj.push(i)

# print(f'Element popped from stack: {obj.pop()}')

# print(obj.get_stack())

# print(obj.peek())
