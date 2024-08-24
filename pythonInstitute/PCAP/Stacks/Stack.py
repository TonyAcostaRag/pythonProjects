
class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, value):
        self.__stack.append(value)

    def pop(self):
        val = self.__stack[-1]
        del self.__stack[-1]
        return val

