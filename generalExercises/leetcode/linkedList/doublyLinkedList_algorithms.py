from dataStructures.Linear.LinkedList.DoublyLinkedList import DoublyLinkedList
from dataStructures.Linear.Node import DualNode


def partition_list(dll, x):
    if dll.head is None:
        return
        
    dummy_one = DualNode(0)
    prev_one = dummy_one
    
    dummy_two = DualNode(0)
    prev_two = dummy_two
    
    current = dll.head
    while current:
    
        if current.value < x:
            prev_one.next = current
            current.prev = prev_one
            current = current.next
            prev_one = prev_one.next
            prev_one.next = None
        
        else:
            prev_two.next = current
            current.prev = prev_two
            current = current.next
            prev_two = prev_two.next
            prev_two.next = None
    
    prev_one.next = dummy_two.next
    if dummy_two.next:
        dummy_two.next.prev = prev_one
    dll.tail = prev_two
    dll.head.prev = None
    return dummy_one.next

def reverse_between(dll, start_index, end_index):
    #   +===================================================+
    #   |               WRITE YOUR CODE HERE                |
    #   | Description:                                      |
    #   | - Reverses a segment of a doubly linked list      |
    #   |   between the given start_index and end_index.    |
    #   | - This operation modifies only the segment in     |
    #   |   place, preserving the rest of the list.         |
    #   |                                                   |
    #   | Behavior:                                         |
    #   | - A dummy node is used to simplify edge cases     |
    #   |   like reversing from the head.                   |
    #   | - The `prev` pointer moves to the node before     |
    #   |   the reversal section.                           |
    #   | - The segment is reversed by removing nodes one   |
    #   |   at a time and reinserting them at the front of  |
    #   |   the sublist.                                    |
    #   | - All `next` and `prev` pointers are updated      |
    #   |   carefully to maintain list integrity.           |
    #   | - At the end, the new head is set properly and    |
    #   |   its prev pointer is cleared.                    |
    #   +===================================================+
    if dll.length < 2 or start_index == end_index:
        return
    
    dummy_node = DualNode(0)
    dummy_node.next = dll.head
    end = dummy_node
    for i in range(end_index + 1):
        
        if i == start_index:
            prev = end
            
        end = end.next
        
    current = prev.next
    for _ in range(end_index - start_index):
        
        to_move = current.next
        temp = prev.next
        
        prev.next = to_move

        if to_move.next:
            to_move.next.prev = current

        current.next = to_move.next
        
        to_move.next = temp
        to_move.prev = prev
        temp.prev = to_move
    
    dll.head = dummy_node.next
    dll.head.prev = None
    return dummy_node.next

def swap_pairs(dll):
    if dll.length < 2:
        return
    
    dummy_node = DualNode(0)
    dummy_node.next = dll.head
    prev = dummy_node
    left = dll.head
    rigth = left.next
    while left and left.next:
        
        rigth = left.next
        
        prev.next = rigth
        rigth.prev = prev
        
        left.next = rigth.next
        if rigth.next:
            rigth.next.prev = left
        
        rigth.next = left
        left.prev = rigth
        
        prev = left
        left = left.next
    
    dll.head = dummy_node.next
    dll.head.prev = None
    return dll.head


if __name__ == '__main__':

    '''
    # Partition List
    my_doubly_linked_list = DoublyLinkedList()
    my_doubly_linked_list.append(5)
    my_doubly_linked_list.append(6)
    my_doubly_linked_list.append(8)
    my_doubly_linked_list.append(9)
    my_doubly_linked_list.append(6)
    my_doubly_linked_list.append(8)
    my_doubly_linked_list.display_nodes_from_head()
    my_doubly_linked_list.head = partition_list(my_doubly_linked_list, 5)
    my_doubly_linked_list.display_nodes_from_head()
    '''

    '''
    # Reverse Between
    my_doubly_linked_list = DoublyLinkedList()
    my_doubly_linked_list.append(3)
    my_doubly_linked_list.append(8)  # 1
    my_doubly_linked_list.append(5)
    my_doubly_linked_list.append(10)
    my_doubly_linked_list.append(2)  # 4
    my_doubly_linked_list.append(1)
    my_doubly_linked_list.display_nodes_from_head()
    start_index = 1
    end_index = 4
    print('Reversing the list...')
    my_doubly_linked_list.head = reverse_between(my_doubly_linked_list,start_index, end_index)
    my_doubly_linked_list.display_nodes_from_head_and_return()
    
    my_doubly_linked_list_two = DoublyLinkedList()
    my_doubly_linked_list_two.append(1)
    my_doubly_linked_list_two.append(2)
    my_doubly_linked_list_two.append(3)
    my_doubly_linked_list_two.append(4)
    my_doubly_linked_list_two.append(5)
    my_doubly_linked_list_two.display_nodes_from_head()
    start_index = 0
    end_index = 4
    my_doubly_linked_list_two.head = reverse_between(my_doubly_linked_list_two, start_index, end_index)
    my_doubly_linked_list_two.display_nodes_from_head_and_return()
    '''


    # Swap pairs
    my_doubly_linked_list_two = DoublyLinkedList()
    my_doubly_linked_list_two.append(1)
    my_doubly_linked_list_two.append(2)
    my_doubly_linked_list_two.append(3)
    my_doubly_linked_list_two.append(4)
    my_doubly_linked_list_two.append(5)
    my_doubly_linked_list_two.display_nodes_from_head_and_return()
    my_doubly_linked_list_two.head = swap_pairs(my_doubly_linked_list_two)
    my_doubly_linked_list_two.display_nodes_from_head_and_return()
