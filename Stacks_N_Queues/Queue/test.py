import unittest
import io

from queue import QueueNode, Queue
from unittest.mock import patch


class TestQueue(unittest.TestCase):

    '''
    The unittest framework follows a set of conventions and hooks for test case classes.
    One of these hooks is the setUp method. When you define a method named setUp in your 
    test case class, the testing framework recognizes it as a setup method. '''
    # The setUp method is called before each test method. 
    '''
    This is done to set up any necessary preconditions or resources that are common to multiple test methods
    isolating the tests from each other and ensures that the outcome of one test does not affect another.
    '''
    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        '''
        By using self.queue.enqueue, you are invoking the enqueue method on the Queue instance that was created in the setUp method.
        '''
        #print("Running test_enqueue...")
        self.queue.enqueue(1)
        self.assertEqual(self.queue.first(), 1)

    def test_dequeue(self):
        #print("Running test_dequeue...")
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.first(), 2)

    
    def test_first_empty_queue(self):
        #print("Running test_first_empty_queue...")
        self.assertIsNone(self.queue.first())

    def test_empty(self):
#       print("Running test_empty...")
        self.assertTrue(self.queue.empty())
        self.queue.enqueue(1)
        self.assertFalse(self.queue.empty())

    def test_print_queue(self):
        print("Running test_print_queue...")
        self.queue.enqueue(1)
        self.queue.enqueue(2)

        printed_output = self.queue.printQueue()

        expected_output = "----\n1\n2\n----"

        #with unittest.mock.patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
        #    self.queue.printQueue()
        
        # output = mock_stdout.getvalue().strip()
        # self.assertEqual(output, "----\n1\n2\n----")
        self.assertEqual(printed_output.strip(), expected_output)


if __name__ == "__main__":
    unittest.main()