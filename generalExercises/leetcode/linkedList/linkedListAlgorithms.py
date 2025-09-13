from dataStructures.Linear.LinkedList.LinkedList import LinkedList
from dataStructures.Linear.Node import _Node


def removeNthFromEnd(ll, n):
    if n < 0:
        return None

    slow = ll._head
    fast = ll._head
    index = 0

    for _ in range(n):

        fast = fast._next
        index += 1
        if fast is None:
            if n == index:
                ll._head = slow._next
                slow._next = None
                return ll._head
            return None
    
    while fast._next:
        slow = slow._next
        fast = fast._next

    if slow._next == fast:
        slow._next = None
    else:
        temp = slow._next._next
        print('slow._next._next:', temp._value)
        slow._next = None
        slow._next = temp
    
    return ll._head

def removeNthFromEnd_solutionApproachOne(ll, n):

    ll_length = 0
    current_node = ll._head

    while current_node:
        current_node = current_node._next
        ll_length += 1

    node_Before_Removed_Index = ll_length - n - 1

    if ll_length == n:
        return ll._head

    current_node = ll._head
    for _ in range(node_Before_Removed_Index):
        current_node = current_node._next

    current_node._next = current_node._next._next

    return ll._head

def removeNthFromEnd_solutionApproachTwo(ll, n):
    fast = ll._head

    for _ in range(n):
        fast = fast._next

    if fast is None:
        return ll.head._next
    
    slow = ll._head

    while fast._next:
        fast = fast._next
        slow = slow._next

    slow._next = slow._next._next

    return ll._head

def remove_duplicated(ll):
        
    current_node = ll._head
    runner = ll._head
    visited_nodes = {}
    
    while current_node:
        
        if runner._value not in visited_nodes:
            
            while runner._next:

                if runner._next._value == current_node._value:
                    runner._next = runner._next._next
                else:
                    runner = runner._next
            
            visited_nodes[current_node._value] = 1

        current_node = current_node._next
        runner = current_node
            
    return ll._head

def remove_node_and_duplicated(ll):
        
    node_occurrences = {}

    dummy_node = _Node(0)

    dummy_node._next = ll._head
    temp = ll._head
    current_node = dummy_node._next
    prev_node = dummy_node

    while temp:

        if temp._value not in node_occurrences:
            node_occurrences[temp._value] = 1
        else:
            node_occurrences[temp._value] += 1
        temp = temp._next
    
    while current_node:
        if node_occurrences[current_node._value] > 1:
            prev_node._next = current_node._next
        else:
            prev_node = current_node
        current_node = current_node._next
    
    return dummy_node._next

def binary_to_decimal(ll):
        
        current_node = ll._head
        binary_numbers = []
        while current_node:
            binary_numbers.append(current_node._value)
            current_node = current_node._next
            
        decimal_number = 0
        exp = 0
        for i in range(len(binary_numbers) - 1, -1, -1):
            if binary_numbers[i] == 1:
                decimal_number += (2 ** exp)
            exp += 1
        
        return decimal_number

def partition_list(ll, threshold):
        
        if ll._size == 0:
            return 
        
        current_node = ll._head
        dummy1 = _Node(0)
        prev1 = dummy1
        dummy2 = _Node(0)
        prev2 = dummy2
        
        while current_node:
            
            if current_node._value < threshold:
                prev1._next = current_node
                current_node = current_node._next
                prev1 = prev1._next
                prev1._next = None
            else:
                prev2._next = current_node
                current_node = current_node._next
                prev2 = prev2._next
                prev2._next = None
        
        prev1._next = dummy2._next
        return dummy1._next

def reverse_list(ll):
    temp = ll._head
    ll._head = ll._tail
    ll._tail = temp
    after = ll._tail._next
    before = None

    while ll._tail:
        after = ll._tail._next
        ll._tail._next = before
        before = ll._tail
        ll._tail = after

    return ll._head


if __name__ == '__main__':

    index_from_end = 2

    my_linked_list = LinkedList()
    my_linked_list.add_node_in_tail(3)
    my_linked_list.add_node_in_tail(8)
    my_linked_list.add_node_in_tail(5)
    my_linked_list.add_node_in_tail(10)
    my_linked_list.add_node_in_tail(2) 
    my_linked_list.add_node_in_tail(1)
    my_linked_list.display_nodes()

    '''
    # Binary link test
    binary_link_list = LinkedList()
    binary_link_list.add_node_in_tail(1)
    binary_link_list.add_node_in_tail(0)
    binary_link_list.add_node_in_tail(0)
    binary_link_list.add_node_in_tail(0)
    binary_link_list.display_nodes()
    '''

    #removeNthFromEnd(my_linked_list, index_from_end)
    #removeNthFromEnd_solutionApproachOne(my_linked_list, index_from_end)
    #removeNthFromEnd_solutionApproachTwo(my_linked_list, index_from_end)

    # Remove duplicated test
    #remove_duplicated(my_linked_list)
    #my_linked_list._head = remove_node_and_duplicated(my_linked_list)
    #my_linked_list.display_nodes()

    # Binary link test
    #print('Decimal representation:', binary_to_decimal(binary_link_list))

    # Partition list test
    '''
    threshold = 5
    partitioned_linked_list = my_linked_list
    partitioned_linked_list._head = partition_list(my_linked_list, threshold)

    print('\nPartitioned list:')
    partitioned_linked_list.display_nodes()
    '''

    # reverse list test
    my_linked_list._head = reverse_list(my_linked_list)
    my_linked_list.display_nodes()
