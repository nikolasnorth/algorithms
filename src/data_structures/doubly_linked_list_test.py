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

    def test_update(self):
        dll = DoublyLinkedList()
        items = [100, 200, 300, 400, 500]
        for item in items:
            dll.insert(item)
        for i in range(len(items)):
            dll[i] = items[i] * 10
            self.assertEqual(dll[i], items[i] * 10, f"incorrect value found at position {i}")

    def test_remove(self):
        dll = DoublyLinkedList()
        items = [100, 200, 300, 400, 500]
        for item in items:
            dll.insert(item)
        # Remove first node
        self.assertEqual(dll.remove(0), 100)
        self.assertEqual(dll[0], 200)
        # Remove last node
        self.assertEqual(dll.remove(len(dll) - 1), 500)
        self.assertEqual(dll[len(dll) - 1], 400)
        # Remove middle node
        self.assertEqual(dll.remove(1), 300)
        self.assertEqual(dll[0], 200)
        self.assertEqual(dll[1], 400)


if __name__ == '__main__':
    unittest.main()
