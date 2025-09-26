from dataStructures.Node import Node


class Stack_LinkedList:

    def __init__(self):
        self.top = None
        self.height = 0

    def push(self, value):
        self.height += 1
        if self.height == 1:
            self.top = Node(value)
            return True
        
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        return True
    
    def pop(self):
        if self.height == 0:
            return None
        
        removed_node = self.top
        self.height -= 1
        if self.height == 0:
            self.top = None
            return removed_node

        self.top = self.top.next
        removed_node.next = None
        return removed_node
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.top
    
    def is_empty(self):
        return self.height == 0
        
    def display_nodes(self):
        current = self.top
        while current:
            print(current.value, end=' -> ')
            current = current.next
        print('Bottom')


if __name__ == '__main__':

    # Push tests
    my_stack = Stack_LinkedList()
    my_stack.push(1)
    my_stack.push(2)
    my_stack.display_nodes()

    # Pop tests
    my_stack.pop()
    my_stack.display_nodes()
    my_stack.pop()
    my_stack.display_nodes()
    my_stack.pop()
    my_stack.display_nodes()
