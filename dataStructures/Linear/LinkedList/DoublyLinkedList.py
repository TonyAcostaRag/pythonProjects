from dataStructures.Node import DualNode


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = DualNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = self.tail.next
        self.length += 1
        return True
    
    def prepend(self, value):
        new_node = DualNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = self.head.prev
        self.length += 1
        return True

    
    def pop(self):
        if self.length == 0:
            return False

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return True
    
    def pop_first(self):

        if self.length == 0:
            return False
        
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1
        return True
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return False
        
        if index <= self.length // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length - 1, index, -1):
                current = current.prev
        return current
    
    def insert_at_index(self, value, index):
        if index < 0 or index > self.length:
            return False
        
        if index <= self.length // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length - 1, index, -1):
                current = current.prev

        new_node = DualNode(value)
        self.length += 1

        if index+1 == self.length:
            current.next = new_node
            new_node.prev = current
            self.tail = new_node
            return True

        prev = current.prev
        current.prev = new_node
        new_node.next = current
        if prev:
            prev.next = new_node
        else:
            self.head = new_node

        new_node.prev = prev
        return True
    
    def set_value(self, value, index):
        if index < 0 or index >= self.length:
            return False
        
        if index <= self.length // 2:
            current = self.head 
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length - 1, index, -1):
                current = current.prev
        
        current.value = value
        return True
    
    def remove_from_index(self, index):
        if index < 0 or index >= self.length:
            return False
        
        if index <= self.length // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length - 1, index, -1):
                current = current.prev
        
        prev = current.prev
        after = current.next
        if prev:
            prev.next = after
        else:
            self.head = after

        if after:
            after.prev = prev
        else:
            self.tail = prev

        self.length -= 1
        current = None
        return current

    def display_nodes_from_head(self):
        print('Printing from head:')
        current = self.head
        print(current.prev, end=' <-> ')
        while current:
            print(current.value, end='')

            if current.next is not None:
                print(' <-> ', end='')
            else:
                print(' <->', current.next)

            current = current.next

    def display_nodes_from_head_and_return(self):

        print('Printing from head and returning to head again:')
        current = self.head
        print(current.prev, end=' <-> ')
        while current:
            print(current.value, end='')

            if current.next is not None:
                print(' <-> ', end='')
                current = current.next
            else:
                last = current
                print(' <->', current.next, end=' <-> ')
                current = current.next
        
        while last:
            print(last.value, end='')

            if last.prev is not None:
                print(' <-> ', end='')
                last = last.prev
            else:
                first = last
                print(' <-> ', last.prev)
                last = last.prev

    def display_nodes_from_tail(self):
        print('Printing from tail:')
        current = self.tail
        while current:
            print(current.value, end='')

            if current.prev is not None:
                print(' <-> ', end='')
            
            current = current.prev
        print()
    

if __name__ == '__main__':

    my_doubly_linked_list = DoublyLinkedList()
    my_doubly_linked_list.append(4)
    my_doubly_linked_list.append(8)
    my_doubly_linked_list.append(10)
    my_doubly_linked_list.display_nodes_from_head()
    #my_doubly_linked_list.display_nodes_from_tail()
    my_doubly_linked_list.pop()
    my_doubly_linked_list.display_nodes_from_head()
    my_doubly_linked_list.pop()
    my_doubly_linked_list.display_nodes_from_head()
    my_doubly_linked_list.pop()
    my_doubly_linked_list.display_nodes_from_head()
    my_doubly_linked_list.pop()
    print('Head:', my_doubly_linked_list.head)
    my_doubly_linked_list.prepend(40)
    print('Head:', my_doubly_linked_list.head.value)
    my_doubly_linked_list.display_nodes_from_head()
    my_doubly_linked_list.append(4)
    my_doubly_linked_list.append(8)
    my_doubly_linked_list.append(10)
    print('Head:', my_doubly_linked_list.head.value)
    my_doubly_linked_list.display_nodes_from_head()
    my_doubly_linked_list.prepend(100)
    print('Head:', my_doubly_linked_list.head.value)
    my_doubly_linked_list.display_nodes_from_head()
    my_doubly_linked_list.pop_first()
    my_doubly_linked_list.display_nodes_from_head()
    my_doubly_linked_list.pop_first()
    my_doubly_linked_list.display_nodes_from_head()
    my_doubly_linked_list.pop_first()
    my_doubly_linked_list.display_nodes_from_head()
    my_doubly_linked_list.pop_first()
    my_doubly_linked_list.display_nodes_from_head()
    my_doubly_linked_list.pop_first()
    my_doubly_linked_list.display_nodes_from_head()
    my_doubly_linked_list.pop_first()
    my_doubly_linked_list.display_nodes_from_head()
    my_doubly_linked_list.append(4)
    my_doubly_linked_list.append(8)
    my_doubly_linked_list.append(10)
    my_doubly_linked_list.append(25)
    my_doubly_linked_list.append(5)
    my_doubly_linked_list.display_nodes_from_head()
    print('Getting the node at index 0:', my_doubly_linked_list.get(0).value)
    print('Getting the node at index 1:', my_doubly_linked_list.get(1).value)
    print('Getting the node at index 2:', my_doubly_linked_list.get(2).value)
    print('Getting the node at index 3:', my_doubly_linked_list.get(3).value)
    print('Getting the node at index 4:', my_doubly_linked_list.get(4).value)
    print('Inserting 1000 in the middle (index=2) of the list:')
    my_doubly_linked_list.insert_at_index(1000, 2)
    my_doubly_linked_list.display_nodes_from_head()
    print('Inserting 0 in the beginning of the list:')
    my_doubly_linked_list.insert_at_index(00, 0)
    my_doubly_linked_list.display_nodes_from_head()
    print('Inserting 2000 in the second half (index=5) of the list:')
    my_doubly_linked_list.insert_at_index(2000, 5)
    my_doubly_linked_list.display_nodes_from_head()
    print('Inserting 3000 a node before the tail (index=7) of the list:')
    my_doubly_linked_list.insert_at_index(3000, 7)
    my_doubly_linked_list.display_nodes_from_head()
    print('Inserting 9000 as the last node (index=9) of the list')
    print(
        '\nHead:', my_doubly_linked_list.head.value,
        '\nTail:', my_doubly_linked_list.tail.value,
        '\nLength:', my_doubly_linked_list.length
    )
    my_doubly_linked_list.insert_at_index(9000, 9)
    my_doubly_linked_list.display_nodes_from_head()
    my_doubly_linked_list.display_nodes_from_tail()

    # Testing the set_value method
    for i in range(my_doubly_linked_list.length):
        my_doubly_linked_list.set_value(i+1, i)
    my_doubly_linked_list.display_nodes_from_head()
    my_doubly_linked_list.display_nodes_from_tail()

    # Testing to verify the exclusion of the range 2nd parameter
    for i in range(my_doubly_linked_list.length-1, 4, -1):
        my_doubly_linked_list.set_value(0, i)
    my_doubly_linked_list.display_nodes_from_head()
    my_doubly_linked_list.display_nodes_from_tail()

    # Testing the remove method
    print('List before removal:')
    my_doubly_linked_list.set_value(10, 9)
    my_doubly_linked_list.display_nodes_from_head()
    my_doubly_linked_list.remove_from_index(4)
    print('List after removal:')
    my_doubly_linked_list.display_nodes_from_head()
    print(
        'Head:', my_doubly_linked_list.head.value,
        '\nTail:', my_doubly_linked_list.tail.value,
        '\nLength:', my_doubly_linked_list.length
    )

    print('\nDeleting the tail:')
    my_doubly_linked_list.remove_from_index(8)
    print('List after removing the tail:')
    my_doubly_linked_list.display_nodes_from_head()
    print(
        'Head:', my_doubly_linked_list.head.value,
        '\nTail:', my_doubly_linked_list.tail.value,
        '\nLength:', my_doubly_linked_list.length
    )

    print('Deleting the head:')
    my_doubly_linked_list.remove_from_index(0)
    print('List after removing the head:')
    my_doubly_linked_list.display_nodes_from_head()
    print(
        'Head:', my_doubly_linked_list.head.value,
        '\nTail:', my_doubly_linked_list.tail.value,
        '\nLength:', my_doubly_linked_list.length
    )
