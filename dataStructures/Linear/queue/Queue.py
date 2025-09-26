from dataStructures.Node import Node


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, value):
        self.length += 1
        if self.length == 1:
            self.head = Node(value)
            self.tail = self.head
            return True
        
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = self.tail.next
        return True
    
    def dequeue(self):
        if self.length == 0:
            return
        
        self.length -= 1
        dequeued_node = self.head
        if self.length == 0:
            self.tail = None
            self.head = self.tail
            return dequeued_node
        
        self.head = self.head.next
        dequeued_node.next = None
        return dequeued_node
    
    def display_nodes(self):

        current = self.head
        while current:
            print(current.value, end=' -> ')
            current = current.next
        print(current)


if __name__ == '__main__':

    my_queue = Queue()
    my_queue.enqueue(1)
    my_queue.enqueue(10)
    my_queue.enqueue(16)
    my_queue.display_nodes()
    my_queue.dequeue()
    my_queue.display_nodes()
    my_queue.dequeue()
    my_queue.display_nodes()
    my_queue.dequeue()
    my_queue.display_nodes()
    my_queue.dequeue()
    my_queue.display_nodes()
