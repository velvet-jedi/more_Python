import unittest  #Python's built-in testing framework.
from unittest.mock import patch
import io   # Provides the interfaces to stream handling. To capture the output of the print function during the dump test.
# Import the Stack and StackNode classes from stack.py
from stack import Stack, StackNode

class TestStack(unittest.TestCase): # defines a test class that inherits from unittest.TestCase.
    def setUp(self):
        # Initialize a new stack for each test case
        # The setUp method is called before each test method. It initializes a new Stack instance (self.stack) for each test.
        self.stack = Stack()

    def test_push_pop(self):
        # pushes 1 onto the stack and asserts that popping from the stack returns 1.
        self.stack.push(1)
        self.assertEqual(self.stack.pop(), 1)
    
    def test_push_multiple_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
    
    def test_pop_empty_stack(self):
        # Test popping from an empty stack should return None
        self.assertIsNone(self.stack.pop())

    def test_count(self):
        self.assertEqual(self.stack.count(), 0)
        self.stack.push(1)
        self.assertEqual(self.stack.count(), 1)
        self.stack.push(2)
        self.assertEqual(self.stack.count(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.count(), 1)

    def test_dump(self):
        # Test dump operation
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        # Redirect stdout to capture the print output
        with unittest.mock.patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            self.stack.dump()
        output = mock_stdout.getvalue().strip()
        # Check if the output matches the expected format
        self.assertEqual(output, "----\n3\n2\n1\n----")

if __name__ == "__main__":
    unittest.main()

''' 
When a Python script is executed, the special variable __name__ is set to "__main__" if the
script is the main program being run. The purpose of this construction is to allow the script to be used both
 as a standalone program and as a module that can be imported into other scripts.
When you run the script directly (e.g., python script_name.py), it executes the tests.
If you import this script as a module in another script (e.g., import script_name),
 the tests won't be automatically executed. This allows you to use the classes and functions defined in the script without triggering the test execution.

ensures that the tests are run only if the script is executed directly, 
not when it's imported as a module. unittest.main() runs the tests defined in the TestStack class

unittest.mock.patch:

This is used to temporarily replace the sys.stdout stream (standard output) with an instance of io.StringIO. io.StringIO is a string buffer that simulates a file, and it allows you to capture the output that would normally be printed to the console.
with ... as mock_stdout::

This is a context manager that ensures the cleanup of resources after the indented block is executed. In this case, it ensures that the patching of sys.stdout is reverted to its original state after the with block.
self.stack.dump():

This line calls the dump method on the self.stack instance. The dump method likely prints the contents of the stack to the standard output.
output = mock_stdout.getvalue().strip():

After the dump method has been called within the patched context, this line retrieves the content that was printed to the standard output using the getvalue() method of mock_stdout. The strip() method is used to remove leading and trailing whitespace.
self.assertEqual(output, "----\n3\n2\n1\n----"):

This line uses self.assertEqual to compare the captured output (output) with the expected format. The expected format is a string with the stack contents in a specific order, separated by newlines.

'''
