from dataStructures.Linear.LinkedListNode import _Node


class StackLinked:

    def __init__(self):
        self._top = None
        self._size = 0

    def get_stack_len(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, element):
        newest = _Node(element)
        if not self.is_empty():
            newest._next_ele = self._top
        self._top = newest
        self._size += 1

    def pop(self):
        if self.is_empty():
            print('Stack is empty!')
            return
        e = self._top._value
        self._top = self._top._next_ele
        self._size -= 1
        if self.is_empty():
            print('Stack is empty!')
        return e

    def get_top_element(self):
        if self.is_empty():
            print('Stack is empty!')
            return
        return self._top._value

    def display(self):
        p = self._top
        while p:
            print(p._value, end=' <-- ')
            p = p._next_ele
        print()


if __name__ == '__main__':
    s = StackLinked()

    s.push('Assembly')
    s.push('C++')
    s.push('Java')
    s.push('Python')

    s.display()