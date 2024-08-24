
from Queues.queue import Queue, QueueError


class AddingQueue(Queue):

    def __init__(self):
        super().__init__()
        self.__totalElements = 0

    def put(self, value):
        super().put(value)
        self.__totalElements += 1

    def get(self):
        if self.__totalElements == 0:
            raise QueueError

        val = super().get()
        self.__totalElements -= 1
        return val

    def get_total_elements(self):
        return self.__totalElements

    def isQueueEmpty(self):
        if self.__totalElements == 0:
            return True
        else:
            return False
