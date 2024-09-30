class CustomStack:

    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.current_size = 0
        self.stack = [] * maxSize

    def push(self, x: int) -> None:
        if self.current_size == self.max_size:
            return None
        self.stack.append(x)
        self.current_size += 1

    def pop(self) -> int:
        if self.current_size == 0:
            return -1
        else:
            element = self.stack.pop()
            self.current_size -= 1
            return element

    def increment(self, k: int, val: int) -> None:
        if k > len(self.stack):
            k = len(self.stack)
        for i in range(k):
            self.stack[i] += val


if __name__ == '__main__':
    obj = CustomStack(3)
    obj.push(1)
    obj.push(2)
    print(obj.stack)
    obj.pop()
    print(obj.stack)
    obj.push(2)
    obj.push(3)
    obj.push(4)
    print(obj.stack)
    obj.increment(5, 100)
    print(obj.stack)
    obj.increment(2, 100)
    print(obj.stack)
    obj.pop()
    obj.pop()
    obj.pop()
    obj.pop()

    print(obj.stack)
