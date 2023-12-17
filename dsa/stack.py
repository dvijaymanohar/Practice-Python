
"""
This stack class supports push, pop, peek and is_empty methods

"""


class Stack():
    """
    Default constructor
    """
    def __init__(self) -> None:
        self.stack_list = []

    """ stack push operation to push an element into the stack"""

    # Parameters:

    # Returns:

    # Example:
    # >>> push(element)
    """
    def push(self, item):
        self.stack_list.insert(item)

    """Stack's pop operation"""
    def pop(self):
        return self.stack_list.pop()


obj = Stack()
obj.push(5)
print("Element popped from stack: " + obj.pop())
