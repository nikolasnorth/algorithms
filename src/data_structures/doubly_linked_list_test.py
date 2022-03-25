import unittest
from doubly_linked_list import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):

    def test_insert(self):
        dll = DoublyLinkedList()
        items = [100, 200, 300, 400, 500]
        for item in items:
            dll.insert(item)
        # Check values were inserted in the correct order
        for i in range(len(items)):
            self.assertEqual(dll[i], items[i], f"incorrect value found at position {i}")
        self.assertEqual(len(dll), len(items))


if __name__ == '__main__':
    unittest.main()
