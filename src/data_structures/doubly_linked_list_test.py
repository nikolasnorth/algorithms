import unittest
from doubly_linked_list import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):

    def test_get_x(self):
        dll = DoublyLinkedList()
        self.assertEqual(dll.get_x(), 5)


if __name__ == '__main__':
    unittest.main()
