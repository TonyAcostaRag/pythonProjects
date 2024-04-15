
class Queue:
    def __init__(self):
        self.__queue = []

    def put(self, value):
        self.__queue.append(value)

    def get(self):
        val = self.__queue.pop(0)
        return val


class QueueError(IndexError):
    pass

