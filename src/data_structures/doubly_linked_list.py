from typing import Optional


class Node:

    def __init__(self, data, nxt=None, prev=None):
        self._data = data
        self._next: Optional[Node] = nxt
        self._prev: Optional[Node] = prev

    def data(self):
        return self._data

    def set_data(self, data):
        self._data = data

    def next(self):
        return self._next

    def set_next(self, nxt):
        self._next = nxt

    def prev(self):
        return self._prev

    def set_prev(self, prev):
        self._prev = prev


class DoublyLinkedList:
    _head: Optional[Node]
    _tail: Optional[Node]
    _size: int

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def head(self):
        return self._head

    def tail(self):
        return self._tail

    def insert(self, data):
        """
        Inserts data at the end of the list.
        :param data: Data
        :return: None
        """
        node = Node(data=data)
        if len(self) == 0:
            self._head = node
            self._tail = node
        else:
            self._tail.set_next(node)
            node.set_prev(self._tail)
            self._tail = node
        self._size += 1

    def remove(self, i: int):
        """
        Removes and returns the data stored at the i-th position.
        :param i:
        :return:
        """
        pass

    def __len__(self):
        return self._size

    def __getitem__(self, i: int):
        """
        Returns the data stored at the i-th position.
        :param i: Index
        :return: Data stored at position `i`
        """
        if i < 0 or i >= len(self):
            raise IndexError
        node = self._head
        for i in range(i):
            node = node.next()
        return node.data()

    def __setitem__(self, i: int, data):
        """
        Stores the given data in the i-th node.
        :param i: Index
        :param data: Data
        :return: None
        """
        pass

    def __delitem__(self, i: int):
        """
        Removes the i-th node from the list.
        :param i: Index
        :return: None
        """
