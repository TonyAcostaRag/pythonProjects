from dataStructures.Linear.LinkedListNode import _Node


class LinkedList:

    def __init__(self):
        self._size = 0
        self._head = None

    def is_empty(self):
        return self._size == 0

    def search(self, key):
        p = self._head
        index = 0
        while p:
            if p._value == key:
                return index
            p = p._next_ele
            index += 1
        return -1

    def insert_sorted(self, element):
        newest = _Node(element)

        if self.is_empty():
            self._head = newest
        else:
            p = self._head
            q = self._head
            
        while p and p._value < element:
            q = p
            p = p._next_ele
        if p == self._head:
            newest._next_ele = self._head
            self._head = newest
        else:
            newest._next_ele = q._next_ele
            q._next_ele = newest
        self._size += 1
