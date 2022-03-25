import unittest
from doubly_linked_list import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):

    def test_insert(self):
        dll = DoublyLinkedList()
        items = [100, 200, 300, 400, 500]
        for item in items:
            dll.insert(item)
        for i in range(len(items)):
            self.assertEqual(dll[i], items[i], f"incorrect value found at position {i}")
        self.assertEqual(len(dll), len(items))

    def test_set(self):
        dll = DoublyLinkedList()
        items = [100, 200, 300, 400, 500]
        for item in items:
            dll.insert(item)
        for i in range(len(items)):
            dll[i] = items[i] * 10
            self.assertEqual(dll[i], items[i] * 10, f"incorrect value found at position {i}")


if __name__ == '__main__':
    unittest.main()
