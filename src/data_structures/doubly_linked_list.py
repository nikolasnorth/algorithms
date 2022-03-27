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

    def insert(self, data, i: int = -1):
        """
        Inserts data at the i-th position. Defaults to the end of the list.
        :param i: Index
        :param data: Data
        :return: None
        """
        node = Node(data=data)
        if len(self) == 0:
            self._head = node
            self._tail = node
        elif i == -1 or i == len(self):
            self._tail.set_next(node)
            node.set_prev(self._tail)
            self._tail = node
        else:
            prev = self._node_prior_to(i)
        self._size += 1

    def remove(self, i: int):
        """
        Removes and returns the data stored at the i-th position.
        :param i: Index
        :return: Data stored at the i-th position
        """
        if i < 0 or i > len(self):
            raise IndexError
        node = self._head
        if len(self) == 1:
            self._head = None
            self._tail = None
        elif i == 0:
            self._head = self._head.next()
            self._head.set_prev(None)
            node.set_next(None)
        elif i == len(self) - 1:
            node = self._tail
            self._tail = self._tail.prev()
            self._tail.set_next(None)
            node.set_prev(None)
        else:
            prev = self._node_prior_to(i)
            node = prev.next()
            prev.set_next(node.next())
            node.next().set_prev(prev)
            node.set_prev(None)
            node.set_next(None)
        self._size -= 1
        return node.data()

    def __len__(self):
        return self._size

    def __getitem__(self, i: int):
        """
        Returns the data stored at the i-th position.
        :param i: Index
        :return: Data stored at position `i`
        """
        return self._node_at(i).data()

    def __setitem__(self, i: int, data):
        """
        Stores the given data in the i-th node.
        :param i: Index
        :param data: Data
        :return: None
        """
        self._node_at(i).set_data(data)

    def __delitem__(self, i: int):
        """
        Removes the i-th node from the list.
        :param i: Index
        :return: None
        """
        self.remove(i)

    def _node_at(self, i: int):
        """
        Returns the node at the i-th position.
        :param i: Index
        :return: Node at position `i`
        """
        if i < 0 or i >= len(self):
            raise IndexError
        node = self._head
        for _ in range(i):
            node = node.next()
        return node

    def _node_prior_to(self, i: int):
        """
        Returns the node prior to the i-th position. If i = 0, then the first node is returned.
        :param i: Index
        :return: Node prior to position `i`
        """
        if i < 0 or i > len(self):
            raise IndexError
        node = self._head
        for _ in range(i - 1):
            node = node.next()
        return node
