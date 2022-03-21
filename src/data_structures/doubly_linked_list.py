from typing import Optional, TypeVar, Generic

T = TypeVar('T')


class Node(Generic[T]):

    def __init__(self, data, nxt=None, prev=None):
        self._data: T = data
        self._nxt: Optional[Node] = nxt
        self._prev: Optional[Node] = prev


class DoublyLinkedList:

    def __init__(self):
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None

    def head(self):
        return self._head

    def tail(self):
        return self._tail
