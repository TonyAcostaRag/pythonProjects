class _Node:

    def __init__(self, value, next_ele=None):
        self._value = value
        self._next_ele = next_ele


class QueuesLinked:

    def __init__(self):
        self.__front = None
        self.__rear = None
        self.__size = 0

    def get_queue_length(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def enqueue(self, value):
        newest = _Node(value)
        if self.is_empty():
            self.__front = newest
        else:
            self.__rear._next_ele = newest
        self.__rear = newest
        self.__size += 1

    def dequeue(self):
        if self.is_empty():
            print('Queue is empty.')
            return
        e = self.__front._value
        self.__front = self.__front._next_ele
        self.__size -= 1
        if self.is_empty():
            self.__rear = None
        return e

    def get_first(self):
        if self.is_empty():
            print('Queue is empty!')
            return
        return self.__front._value

    def display(self):
        p = self.__front
        while p:
            print(p._value, end=' <-- ')
            p = p._next_ele
        print()


if __name__ == '__main__':
    Queue = QueuesLinked()
    Queue.enqueue(5)
    Queue.enqueue(7)
    Queue.enqueue(10)
    print('Length:', Queue.get_queue_length())
    Queue.display()
