
from Stacks.Stack import Stack


class AddingStack(Stack):
    def __init__(self):
        super().__init__()
        self.__sum_Values = 0
        self.__sum_Total_Pushes = 0
        self.__sum_Total_Pops = 0

    def push(self, value):
        self.__sum_Values += value
        self.__sum_Total_Pushes += 1
        super().push(value)

    def pop(self):
        val = super().pop()
        self.__sum_Values -= val
        self.__sum_Total_Pops += 1
        return val

    def get_sum(self):
        return self.__sum_Values

    def get_total_pushes(self):
        return self.__sum_Total_Pushes

    def get_total_pops(self):
        return self.__sum_Total_Pops
