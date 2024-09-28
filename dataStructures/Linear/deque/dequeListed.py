class MyCircularDeque:

    def __init__(self, k: int):
        self.max_size = k
        self.head = None
        self.tail = None
        self.current_size = 0
        self.queue = [] * k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.isEmpty():
            self.tail = value

        temp_list = [value]
        for i in self.queue:
            temp_list.append(i)
        self.queue = temp_list
        self.head = self.queue[0]

        self.current_size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.isEmpty():
            self.head = value

        self.queue.append(value)
        self.tail = self.queue[-1]

        self.current_size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        temp_list = []
        for i in range(1, len(self.queue)):
            temp_list.append(self.queue[i])
        self.queue = temp_list
        self.current_size -= 1
        if self.isEmpty():
            self.head = None
        else:
            self.head = self.queue[0]
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.queue.pop()
        self.current_size -= 1
        if self.isEmpty():
            self.tail = None
        else:
            self.tail = self.queue[-1]
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.head

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.tail

    def isEmpty(self) -> bool:
        return self.current_size == 0

    def isFull(self) -> bool:
        return self.current_size == self.max_size


if __name__ == '__main__':

    obj = MyCircularDeque(10)
    print(obj.insertFront(10))
    print(obj.insertLast(5))
    print(obj.deleteFront())
    print(obj.deleteLast())
    print(obj.getFront())
    print(obj.getRear())
    print(obj.isEmpty())
    print(obj.isFull())

    obj = MyCircularDeque(5)

    print('Insert:', obj.insertFront(7))
    print(obj.queue)
    print('Insert:', obj.insertLast(0))
    print(obj.queue)
    print(obj.getFront())
    print('Insert:', obj.insertLast(3))
    print(obj.queue)
    print(obj.getFront())
    print('Insert:', obj.insertFront(9))
    print(obj.queue)
    print(obj.getRear())
    print(obj.getFront())
    print(obj.getFront())
    print(obj.deleteLast())
    print(obj.queue)
    print(obj.getRear())
