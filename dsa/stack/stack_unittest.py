import unittest
from stack import Stack


class TestStack(unittest.TestCase):
    """Create an instance of the Stack class for each test

    Args:
        unittest (_type_): _description_
    """

    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        """Test function to test the push operation of stack
        """
        for i in range(0, 10):
            result, status = self.stack.push(i)

            if not status:
                self.assertEqual(result, 0, "Addition successful")
            else:
                self.assertEqual(result, 0, "Addition not successful")

    def test_pop(self):
        """Test function to test the pop operation of the stack
        """

        self.test_push()

        result, status = self.stack.pop()

        if status:
            self.assertEqual(result, 0, "Pop operation not successful")
        else:
            print(f'Element popped: {result}')

    def test_peek(self):
        """Test function to return the top of the stack without poping
        """

        self.test_push()

        result, status = self.stack.peek()

        if status:
            self.assertEqual(result, 0, "Peek operation not successful")
        else:
            print(f'Element at top: {result}')

    def test_get_stack(self):
        """Get the list in the stack
        """
        result, status = self.stack.get_stack()
        if status:
            self.assertEqual(result, 0, "Peek operation not successful")
        else:
            print(f'Element at top: {result}')


if __name__ == "__main__":
    unittest.main()
