from dataStructures.Node import Node


class Stack_twoQueues:

    def __init__(self):
        self.front_one = None
        self.tail_one = None
        self.height_one = 0

        self.front_two = None
        self.tail_two = None

        self.top_item = 0

    def push(self, value):
        self.top_item = value
        self.height_one += 1
        if self.front_one is None:
            self.front_one = Node(value)
            self.tail_one = self.front_one
        else:
            self.tail_one.next = Node(value)
            self.tail_one = self.tail_one.next
    
    def pop(self):
        if self.height_one == 0:
            return

        while self.front_one and self.front_one.next:
            removed_one_element = self.front_one
            self.front_one = self.front_one.next
            removed_one_element.next = None
            self.top_item = removed_one_element.value
            if self.front_two is None:
                self.front_two = removed_one_element
                self.tail_two = self.front_two
            else:
                self.tail_two.next = removed_one_element
                self.tail_two = self.tail_two.next
            removed_one_element = None

        poped_element = self.front_one.value
        self.height_one -= 1
        self.front_one = None
        self.tail_one = None

        while self.front_two:
            removed_two_element = self.front_two
            self.front_two = self.front_two.next
            removed_two_element.next = None
            if self.front_one is None:
                self.front_one = removed_two_element
                self.tail_one = removed_two_element
            else:
                self.tail_one.next = removed_two_element
                self.tail_one = self.tail_one.next
            removed_two_element = None
            
            if self.front_two is None:
                self.tail_two = None
        
        return poped_element
    
    def top(self) -> int:
        return self.top_item

    def empty(self) -> bool:
        return self.height_one == 0
    
    def display_stack(self):

        current = self.front_one
        if current is None:
            print(current)
        while current:
            print(current.value, ' -> ', end='')
            current = current.next
            if current is None:
                print(current)


if __name__ == '__main__':

    my_stack = Stack_twoQueues()
    my_stack.push(1)
    print('Top:', my_stack.top())
    my_stack.push(2)
    print('Top:', my_stack.top())
    my_stack.push(3)
    print('Top:', my_stack.top())

    print('Poped element:', my_stack.pop())
    print('Top:', my_stack.top())
    print('Poped element:', my_stack.pop())
    print('Top:', my_stack.top())
    print('Poped element:', my_stack.pop())
    print('Top:', my_stack.top())

    print('Is empty:', my_stack.empty())
    my_stack.display_stack()
