from dataStructures.Linear.LinkedList.LinkedList import LinkedList
from dataStructures.Node import _Node
import huge_imput_data as input
import math
import time


def findMiddleNode(ll):
    slow = ll._head
    fast = ll._head

    while fast and fast._next:
        slow = slow._next
        fast = fast._next._next
    
    return slow._value

def cycle_tail_at_index(ll, index):
    pointer = ll._head
    i = 0
    while i < index:
        pointer = pointer._next
        i += 1
    ll._tail._next = pointer

def cycle_tail_at_head(ll):
    pointer = ll._head
    while pointer and pointer._next:
        #print('cycle tail -- node:', pointer._value)
        pointer = pointer._next

    #print('Cycling list head from node:', pointer._value)
    pointer._next = ll._head

def hasLoop(ll):
    slow = ll._head
    fast = ll._head

    while fast and fast._next:
        slow = slow._next
        fast = fast._next._next

        if slow == fast:
            return True
    
    return False

def hasLoopAtNode(ll):
    slow = ll._head
    fast = ll._head

    while fast and fast._next:
        #print('Finding the loop -- node:', slow._value)
        slow = slow._next
        fast = fast._next._next

        if slow == fast:
            #print('Loop at node:', slow._value)
            return slow._value

    return None

def findKthNodeFromEnd(ll, index_from_end):
    prev = ll._head
    front = ll._head

    for _ in range(index_from_end):
        front = front._next
    
    while front._next:
        prev = prev._next
        front = front._next
    
    return prev._next._value

def remove_duplicate_nodes_udemy(ll):

    current_node = ll._head
    runner = current_node
    while current_node:

        while runner._next:
            if runner._next._value == current_node._value:
                runner._next = runner._next._next
            else:
                runner = runner._next
        
        current_node = current_node._next
        runner = current_node

def remove_all_duplicated_nodes_udemy(ll):
    node_count = {}
    current_node = ll._head
    while current_node:
        if current_node._value not in node_count:
            node_count[current_node._value] = 1
        else:
            node_count[current_node._value] += 1
        current_node = current_node._next
    
    dummy1 = _Node(0)
    dummy1._next = ll._head
    prev = dummy1
    current_node = ll._head
    while current_node:
        if node_count[current_node._value] > 1:
            if current_node == ll._head:
                ll._head = ll._head._next
            current_node = current_node._next
            prev._next = current_node
        else:
            current_node = current_node._next
            prev = prev._next

def binary_to_decimal(ll):
    binary_array = []
    current_node = ll._head
    while current_node:
        binary_array.append(current_node._value)
        current_node = current_node._next

    decimal_number = 0
    exp = 0
    for i in range(len(binary_array)-1, -1, -1):
        if binary_array[i] == 1:
            decimal_number += 2**exp
        exp += 1
    
    return decimal_number

def partition_list(ll, threshold):
    # time complexity: O(n)
    dummy_one = _Node(0)
    dummy_two = _Node(0)
    prev1 = dummy_one
    prev2 = dummy_two
    current_node = ll._head

    while current_node:  # O(n)
        
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
    
    prev1._next = dummy_two._next
    return dummy_one._next

def reverse_list_udemy(ll):
    # time complexity: O(n)
    temp = ll._head
    ll._head = ll._tail
    ll._tail = temp
    before = None
    after = temp._next

    while temp:  # O(n)
        after = temp._next
        temp._next = before
        before = temp
        temp = after
    
    return ll._head

def reverse_list(ll):

    actualHead = ll._head
    while ll._head and ll._head._next:
        afterHead = ll._head._next
        ll._head._next = afterHead._next
        afterHead._next = actualHead
        actualHead = afterHead
    ll._head = actualHead
    return ll._head

def reverse_between_udemy(ll, start_index, end_index):

    if ll._size == 0:
        return None

    if start_index == end_index:
        return ll._head
    
    dummy_node = _Node(0)
    dummy_node._next = ll._head
    
    prev = dummy_node
    index = 0
    while index < start_index:
        prev = prev._next
        index += 1
    
    current = prev._next
    to_move = current._next
    index = 0
    while index + start_index < end_index:
        
        temp = prev._next
        prev._next = to_move
        current._next = to_move._next
        to_move._next = temp
        
        to_move = current._next
        index += 1
    
    ll._head = dummy_node._next
    return ll._head

def swap_node_pairs(ll):

    if ll._size == 0:
        return 

    dummy_node = _Node(0)
    prev = dummy_node
    dummy_node._next = ll._head
    current = prev._next
    while current and current._next:
        pair = current._next
        prev._next = pair
        current._next = pair._next
        pair._next = current

        prev = current
        current = current._next

    ll._head = dummy_node._next
    return ll._head

def intersectionNode_HashMap(ll1, ll2):
    #  Space complexity: O(m+n)
    if ll1._head is None or ll2._head is None:
        return None
    
    if ll1._head == ll2._head:
        return ll1._head
    
    current_node = ll1._head
    listA = []
    while current_node:
        
        if current_node.val not in listA:
            listA.append(current_node)
        current_node = current_node.next
    
    current_node = ll2._head
    listB = []
    while current_node:
        
        if current_node.val not in listB:
            listB.append(current_node)
        current_node = current_node.next
            
    cursor = 0
    total_iterations = 0
    if len(listA) < len(listB):
        total_iterations = len(listB)
    else:
        total_iterations = len(listA)
        
    temp = None
    while (total_iterations-cursor) >= 0:
        
        if listA[len(listA)-1-cursor] != listB[len(listB)-1-cursor]:
            return temp
        temp = listA[len(listA)-1-cursor]
        cursor += 1

def list_interceptor(intercepted_list, intercepting_list, index_to_intercept):

    ll = intercepted_list
    interceptor = ll._head
    for _ in range(index_to_intercept):
        interceptor = interceptor._next
        
    intercepting_list_tail = intercepting_list._head
    while intercepting_list_tail._next:
        intercepting_list_tail = intercepting_list_tail._next

    intercepting_list_tail._next = interceptor

def intersectionNode_TwoPointers(ll1, ll2):
    # Time complexity: O(n + m)
    # Space complexity: O(1)
    if ll1._head is None or ll2._head is None:
            return None
        
    if ll1._head == ll2._head:
        return ll1._head
    
    current_node = ll1._head
    lengthA = 0
    while current_node:
        current_node = current_node._next
        lengthA += 1
    
    current_node = ll2._head
    lengthB = 0
    while current_node:
        current_node = current_node._next
        lengthB += 1
            
    if lengthA < lengthB:
        small_pointer = ll1._head
        larger_pointer = ll2._head
        difference = lengthB - lengthA
    else:
        small_pointer = ll2._head
        larger_pointer = ll1._head
        difference = lengthA - lengthB

    for _ in range(difference):
        larger_pointer = larger_pointer._next
        
    while small_pointer:
        
        if small_pointer == larger_pointer:
            return small_pointer
        small_pointer = small_pointer._next
        larger_pointer = larger_pointer._next

def isPalindrome(ll):
        
    def reverse_after_node(prev):
        
        actualHead = prev._next
        current = actualHead
        while current and current._next:
            after = current._next
            current._next = after._next
            after._next = actualHead
            actualHead = after
        return actualHead
    
    slow = ll._head
    fast = ll._head
    while fast._next and fast._next._next:
        slow = slow._next
        fast = fast._next._next
        
    second_half = reverse_after_node(slow)
    
    current = ll._head
    while second_half:
        
        if current._value != second_half._value:
            return False
        
        current = current._next
        second_half = second_half._next
        
    slow._next = reverse_after_node(slow)
    return True

def mergeTwoLists(ll1, ll2):
    dummy_node = _Node(0)
    pointer = dummy_node

    current1 = ll1._head
    current2 = ll2._head

    while current1 and current2:
        if current1._value < current2._value:
            pointer._next = current1
            current1 = current1._next
            pointer = pointer._next
            pointer._next = None
        elif current1._value >= current2._value:
            pointer._next = current2
            current2 = current2._next
            pointer = pointer._next
            pointer._next = None

    if current1 is None:
        pointer._next = current2
    else:
        pointer._next = current1
    
    return dummy_node._next
    
def deleteNnodesAfterMnodes(ll, m, n):

    current = ll._head
    after = current._next
    counter = 1
    while current and current._next:
        after = current._next
        if (m - counter) == 0:
            counter = 0
        
            for _ in range(n):
                if after:
                    current._next = after._next
                    after = current._next

        current = current._next
        counter += 1

    return ll._head

def linkedListFrequency_counting_freq(ll):
    numbers_frequency = {}
    current = ll._head
    while current:
        
        if current._value not in numbers_frequency:
            numbers_frequency[current._value] = 1
        else:
            numbers_frequency[current._value] += 1
        current = current._next
    
    dummy_node = _Node(0)
    prev = dummy_node

    for i in numbers_frequency.values():
        prev._next = _Node(i)
        prev = prev._next
        prev._next = None

    return dummy_node._next

def linkedListFrequency(ll):

    number_frequency = {}
    freqListHead = None
    current = ll._head
    while current:

        if current._value in number_frequency:
            freqNode = number_frequency[current._value]
            freqNode._value += 1
        else:
            newFreqNode = _Node(1)
            newFreqNode._next = freqListHead
            number_frequency[current._value] = newFreqNode
            freqListHead = newFreqNode
        current = current._next

    return freqListHead

def addTwoNumbers_5n(ll1, ll2):
    number_one_head = None
    number_two_head = None

    current1 = ll1._head
    while current1:

        new_node = _Node(current1._value)
        new_node._next = number_one_head
        number_one_head = new_node
        current1 = current1._next

    number_one = 0
    current1 = number_one_head
    while current1:

        if number_one == 0:
            number_one += current1._value
        else:
            number_one = (number_one * 10) + current1._value
        current1 = current1._next

    current2 = ll2._head
    while current2:

        new_node = _Node(current2._value)
        new_node._next = number_two_head
        number_two_head = new_node
        current2 = current2._next

    number_two = 0
    current2 = number_two_head
    while current2:

        if number_two == 0:
            number_two += current2._value
        else:
            number_two = (number_two * 10) + current2._value
        current2 = current2._next

    total = number_one + number_two
    total_head = None
    for i in range(len(str(total))):
        new_node = _Node(int(str(total)[i]))
        new_node._next = total_head
        total_head = new_node
    
    return total_head

def addTwoNumbers(ll1, ll2):
    
    current1 = ll1._head
    current2 = ll2._head
    remainder = 0
    dummy_node = _Node(0)
    prev = dummy_node
    while current1 and current2:
        
        val = remainder + current1._value + current2._value
        remainder -= remainder

        if val > 9:
            val = val - 10
            new_node = _Node(val)
            remainder += 1
        else:
            new_node = _Node(val + remainder)
            remainder = 0
        
        prev._next = new_node
        prev = prev._next
        current1 = current1._next
        current2 = current2._next
    
    def sum_remainder_list(current_node, remainder, previous_node):

        while current_node:
            val = remainder + current_node._value
            remainder -= remainder
            if val > 9:
                val = val - 10
                remainder += 1
            
            new_node = _Node(val)
            previous_node._next = new_node
            previous_node = previous_node._next
            current_node = current_node._next

        return (previous_node, remainder)

    if current1:
        prev, remainder = sum_remainder_list(current1, remainder, prev)

    if current2:
        prev, remainder = sum_remainder_list(current2, remainder, prev)

    if remainder > 0:
        prev._next = _Node(remainder)

    return dummy_node._next

def rotateList_inner_for_loop(ll, rotates_amount):

    if ll._head is None:
        return
    
    dummy_node = _Node(0)
    dummy_node._next = ll._head

    length = 1
    current = ll._head
    while current and current._next:
        length += 1
        current = current._next

    for _ in range(rotates_amount % length):

        current = ll._head
        prev = dummy_node
        while current and current._next:
            current = current._next
            prev = prev._next
        
        temp = dummy_node._next
        dummy_node._next = prev._next
        prev._next = None
        current._next = temp
        ll._head = current

    return dummy_node._next

def rotateList(ll, rotates_amount):
    
    if ll._head is None:
        return                  # 1
    
    current = ll._head          # 2
    length = 1                  # 3
    while current and current._next:    # O(n)
        current = current._next # 4
        length += 1             # 5

    eq_rotations = rotates_amount % length      # 6
    if eq_rotations == 0:
        return ll._head         # 7
    
    dummy_node = _Node(0)       # 8
    dummy_node._next = ll._head # 9
    cut = dummy_node            # 10
    for _ in range(length - eq_rotations):
        cut = cut._next         # 11

    temp = ll._head             # 12
    dummy_node._next = cut._next # 13
    cut._next = None            # 14

    current._next = temp        # 15
    return dummy_node._next     # 16

def rotateList_cyclying(ll, rotates_amount):

    if ll._head is None:        
        return ll._head         # 1
    
    current = ll._head          # 2
    length = 1                  # 3
    while current and current._next:     #  O(n)
        length += 1             # 4
        current = current._next # 5

    current._next = ll._head    # 6
    
    actual_rotations = rotates_amount % length      # 7
    if actual_rotations == 0:
        return ll._head         # 8
    
    to_move = ll._head          # 9
    for _ in range(length - actual_rotations - 1):  
        to_move = to_move._next # 10

    ll._head = to_move._next    # 11
    to_move._next = None        # 12
    return ll._head             # 13

def deleteDuplicates_2n(ll):
    
    if ll._head is None:
        return
    
    current = ll._head
    ocurrences = {}
    while current:

        if current._value not in ocurrences:
            ocurrences[current._value] = 1
        else:
            ocurrences[current._value] += 1
        current = current._next

    dummy_node = _Node(0)
    dummy_node._next = ll._head
    current = dummy_node
    after = current._next
    while after:

        if ocurrences[current._next._value] > 1:
            if current._next == ll._head:
                ll._head = ll._head._next
            
            current._next = after._next
            after = current._next
        else:
            current = current._next
            after = current._next

def deleteDuplicates(ll):
    
    if ll._head is None:
        return 
    
    dummy_node = _Node(0)
    dummy_node._next = ll._head
    prev = dummy_node
    current = ll._head
    while current and current._next:
        after = current._next

        if current._value == after._value:
            
            while after and current._value == after._value:
                after = after._next

            if ll._head == current:
                ll._head = after
            current = after
            prev._next = after

        else:
            prev = prev._next
        
        current = prev._next

    return dummy_node._next

def reverse_between(ll, start_index, end_index):
    
    dummy_node = _Node(0)
    dummy_node._next = ll._head
    prev = dummy_node
    for _ in range(start_index):
        prev = prev._next

    index = 0
    current = prev._next
    while(start_index + index < end_index):
        to_move = current._next
        temp = prev._next
        prev._next = to_move
        current._next = to_move._next
        to_move._next = temp
        index += 1
    
    return dummy_node._next

def reorderList(ll):
    
    slow = ll._head
    fast = ll._head
    while fast._next and fast._next._next:
        slow = slow._next
        fast = fast._next._next

    current = slow._next
    while current and current._next:
        to_move = current._next
        temp = slow._next
        slow._next = to_move
        current._next = to_move._next
        to_move._next = temp
    
    dummy_node = _Node(0)
    prev = dummy_node
    first_half = ll._head
    second_half = slow._next
    while second_half:
        prev._next = first_half
        first_half = first_half._next
        prev = prev._next
        prev._next = second_half
        second_half = second_half._next
        prev = prev._next

    if first_half == slow:
        prev._next = slow
        prev = prev._next
        prev._next = None

def plusOneLinkedList(ll):
    dummy_node = _Node(0)
    dummy_node._next = ll._head
    notNine = dummy_node
    current = ll._head
    while current:
        if current._value < 9:
            notNine = current
        current = current._next

    if notNine != dummy_node:
        notNine._value += 1
    else:
        temp = notNine._next
        dummy_node._next = _Node(1)
        notNine = notNine._next
        notNine._next = temp
        ll._head = dummy_node._next
    
    notNine = notNine._next
    while notNine:
        notNine._value = 0
        notNine = notNine._next

    return dummy_node._next

def addTwoNumbersII_no_reverse_two_pointers(l1, l2):

    curr1 = l1._head
    len1 = 1
    while curr1 and curr1._next:
        curr1 = curr1._next
        len1 += 1

    curr2 = l2._head
    len2 = 1
    while curr2 and curr2._next:
        curr2 = curr2._next
        len2 += 1

    dummy_node = _Node(0)
    prev = dummy_node
    if len1 >= len2:
        dummy_node._next = l1._head
        len_diff = len1 - len2
        sum_large = l1._head
        sum_short = l2._head
    else:
        dummy_node._next = l2._head
        len_diff = len2 - len1
        sum_large = l2._head
        sum_short = l1._head

    for _ in range(len_diff):
        if sum_large._value != 9:
            prev = sum_large
        sum_large = sum_large._next
    
    while sum_large:
        sum = sum_large._value + sum_short._value
        if sum > 9:
            sum_large._value = sum - 10

            prev._value += 1
            prev = prev._next
            while prev != sum_large:
                prev._value = 0
                prev = prev._next
        else:
            sum_large._value = sum

        if sum < 9:
            prev = sum_large
        sum_large = sum_large._next
        sum_short = sum_short._next

    return dummy_node if dummy_node._value else dummy_node._next

def splitListToParts(ll, k):

        current = ll._head
        len = 0
        while current:
            current = current._next
            len += 1

        nodes_on_pack = len // k
        leftover = len % k

        current = ll._head
        prev = ll._head
        grand_pack = []
        while current:

            ll._head = current
            for _ in range(nodes_on_pack):
                prev = current
                current = current._next
            
            if leftover:
                prev = current
                current = current._next
                leftover -= 1
            
            prev._next = None
            grand_pack.append(ll._head)

        if nodes_on_pack == 0:
            
            for _ in range(k - len%k):
                grand_pack.append(None)

        return grand_pack

def removeZeroSumSublists(ll):

    node_map = {}
    sum = 0
    front = _Node(0)
    front._next = ll._head
    current = front
    while current:
        sum += current._value
        node_map[sum] = current
        current = current._next

    current = front
    sum = 0
    while current:
        sum += current._value
        current._next = node_map[sum]._next
        current = current._next
    
    return front._next

def mergeInBetween(list1, a, b, list2):

    dummy_node = _Node(0)
    dummy_node._next = list1._head
    current_one = dummy_node
    for _ in range(a):
        current_one = current_one._next

    removal__range = current_one
    current_one = current_one._next
    removal__range._next = list2._head
    for _ in range(b - a):
        current_one = current_one._next

    removal__range = current_one._next
    current_two = list2._head
    while current_two and current_two._next:
        current_two = current_two._next

    current_two._next = removal__range
    return dummy_node._next
        
def swapNodes(ll, k):

    length_p = ll._head
    length = 1
    while length_p:
        length += 1
        length_p = length_p._next

    if k > length:
        return

    dummy_node = _Node(0)
    dummy_node._next = ll._head

    prev_swap = dummy_node
    for _ in range(k - 1):
        prev_swap = prev_swap._next
    
    k_start = prev_swap._next
    stop = k_start
    pre_k_end = dummy_node
    while stop and stop._next:
        pre_k_end = pre_k_end._next
        stop = stop._next

    k_end = pre_k_end._next

    temp = k_end._value
    k_end._value = k_start._value
    k_start._value = temp

    return dummy_node._next

def nodesBetweenCriticalPoints(ll):

    if ll._head._next._next is None:
            return [-1, -1]

    prev = ll._head
    current = prev._next
    after = current._next
    critical_points = []
    critical_point_visited = False
    critital_point_distance = 0

    while after:

        if (current._value > prev._value and current._value > after._value) or (current._value < prev._value and current._value < after._value):
            
            if critical_point_visited == False:
                critical_point_visited = True
            else:
                critital_point_distance += 1
            
            critical_points.append(critital_point_distance)
            critital_point_distance = 0
        
        else:
            if critical_point_visited:
                critital_point_distance += 1

        prev = prev._next
        current = prev._next
        after = current._next

    if len(critical_points) <= 1:
        return [-1, -1]

    min = float('inf')
    sum = 0
    for i in range(len(critical_points)):

        sum += critical_points[i]
        if critical_points[i] != 0 and critical_points[i] < min:
            min = critical_points[i]

    return [min, sum]

def reverseEvenLengthGroups(ll):

    dummy_node = _Node(0)
    dummy_node._next = ll._head
    prev = dummy_node
    current = ll._head
    grp_amt = 1
    node_count = 0
    grp_length = 1

    while current and current._next:

        grp_length = 1
        node_length_meter = current
        while grp_length < grp_amt and node_length_meter._next:
            node_length_meter = node_length_meter._next
            grp_length += 1

        if grp_length % 2 == 0:
            node_count += 1
            while node_count < grp_length:

                to_move = current._next
                temp = prev._next
                prev._next = to_move
                node_count += 1
                current._next = to_move._next
                to_move._next = temp
            current = current._next

            for _ in range(grp_length):
                prev = prev._next

        else:
            while current._next and node_count < grp_amt:
                
                current = current._next
                prev = prev._next
                node_count += 1

        if node_count == grp_amt:
            grp_amt += 1
            node_count = 0

    return ll._head

def spiralMatrix(m, n, ll):

    nodes_matrix = [[-1 for _ in range(m)] for _ in range(n)]  # 1

    for row in range(n):
        for col in range(m):
            print(nodes_matrix[row][col], end=' ')
        print()

    row = 0
    col = 0
    current_direction = 0  # 1 Variable para indexar el arreglo direction
    direction = [(0, 1), (1, 0),
                 (0, -1), (-1, 0)]  # 1 Lista ordenada para avanzar en sentido horario
    
    current = ll._head
    while current:

        nodes_matrix[row][col] = current._value
        row += direction[current_direction][0]  # 1 Incrementar con el valor de direction correspondiente
        col += direction[current_direction][1]  # 1

        if (
            row >= n
            or col >= m
            or row < 0
            or col < 0
            or nodes_matrix[row][col] != -1 
        ):
            
            row -= direction[current_direction][0]
            col -= direction[current_direction][1]
            current_direction = (current_direction + 1) % 4     # 1 Cambiar la direccion sentido horario
            row += direction[current_direction][0]
            col += direction[current_direction][1]

        current = current._next

    for row in range(n):
        for col in range(m):
            print(nodes_matrix[row][col], end=' ')
        print()
    
    return nodes_matrix

def splitCircularLinkedList(list):

    head = list._head
    slow = head
    fast = head
    counter = 0
    while slow != fast or counter <= 1:
        slow = slow._next
        counter += 1
        fast = fast._next._next

    current = head
    for _ in range(math.ceil(counter / 2) - 1):
        current = current._next

    second = current._next
    sec_head = current._next
    after_sec = second._next

    current._next = head
    while after_sec != head:
        after_sec = after_sec._next
        second = second._next
    
    second._next = sec_head
    return [head._value, sec_head._value]

def insertGreatestCommonDivisors(ll):

    num_one = ll._head
    while num_one and num_one._next:
        num_two = num_one._next 

        if num_one._value <= num_two._value:
            smallest = num_one._value
        else:
            smallest = num_two._value

        while num_one._value % smallest != 0 or num_two._value % smallest != 0: 
            smallest -= 1

        num_one._next = _Node(smallest)
        num_one = num_one._next
        num_one._next = num_two
        num_one = num_one._next
    
    return ll._head

def modifiedList(nums, ll):

    dummy_node = _Node(0)
    dummy_node._next = ll._head
    prev = dummy_node
    stored_num = {}
    for i in range(len(nums)):
        if nums[i] not in stored_num:
            stored_num[nums[i]] = 1

    while prev._next:
        if prev._next._value in stored_num:
            prev._next = prev._next._next
        else:
            prev = prev._next

    return dummy_node._next


if __name__ == '__main__':

    my_odd_linked_list = LinkedList()
    my_odd_linked_list.add_node_in_tail(1)
    my_odd_linked_list.add_node_in_tail(2)
    my_odd_linked_list.add_node_in_tail(3)
    my_odd_linked_list.add_node_in_tail(4)
    my_odd_linked_list.add_node_in_tail(5)
    my_odd_linked_list.add_node_in_tail(6)
    my_odd_linked_list.add_node_in_tail(7)
    my_odd_linked_list.add_node_in_tail(8)
    my_odd_linked_list.add_node_in_tail(9)
    my_odd_linked_list.add_node_in_tail(10)
    my_odd_linked_list.add_node_in_tail(11)
    my_odd_linked_list.add_node_in_tail(12)
    my_odd_linked_list.add_node_in_tail(13)
    
    my_even_linked_list = LinkedList()
    my_even_linked_list.add_node_in_tail(1)
    my_even_linked_list.add_node_in_tail(2)
    my_even_linked_list.add_node_in_tail(3)
    my_even_linked_list.add_node_in_tail(4)
    my_even_linked_list.add_node_in_tail(5)
    my_even_linked_list.add_node_in_tail(6)
    my_even_linked_list.add_node_in_tail(7)
    my_even_linked_list.add_node_in_tail(8)
    my_even_linked_list.add_node_in_tail(9)
    my_even_linked_list.add_node_in_tail(10)

    '''
    # Middle node:
    print('\nOdd linked list:')
    my_odd_linked_list.display_nodes()
    print('Middle Node:', findMiddleNode(my_odd_linked_list))

    print('\nEven linked list:')
    my_even_linked_list.display_nodes()
    print('Middle Node:', findMiddleNode(my_even_linked_list))
    '''

    '''
    # Has Loop:
    cycle_index = 0
    print('\nOdd linked list has loop:', hasLoop(my_odd_linked_list))
    print('Even linked list has loop:', hasLoop(my_even_linked_list))
    print('Cycling list at node', cycle_index, cycle_tail_at_index(my_odd_linked_list, cycle_index))
    print('Odd linked list has loop:', hasLoop(my_odd_linked_list))
    print('Odd linked list has loop at node:', hasLoopAtNode(my_odd_linked_list))
    print('Even linked list has loop:', hasLoop(my_even_linked_list))
    print('Even linked list has loop at node:', hasLoopAtNode(my_even_linked_list))
    my_odd_linked_list.display_nodes()
    '''

    '''
    # Find the Kth node from end
    my_even_linked_list.display_nodes()
    index_from_end = 4
    print('\nKth node from end:', findKthNodeFromEnd(my_even_linked_list, index_from_end))
    '''

    '''
    # Remove duplicated nodes
    duplicated_nodes_linked_list = LinkedList()
    duplicated_nodes_linked_list.add_node_in_tail(1)
    duplicated_nodes_linked_list.add_node_in_tail(1)
    duplicated_nodes_linked_list.add_node_in_tail(2)
    duplicated_nodes_linked_list.add_node_in_tail(3)
    duplicated_nodes_linked_list.add_node_in_tail(1)
    duplicated_nodes_linked_list.add_node_in_tail(4)
    duplicated_nodes_linked_list.add_node_in_tail(2)
    duplicated_nodes_linked_list.add_node_in_tail(5)
    duplicated_nodes_linked_list.add_node_in_tail(5)
    duplicated_nodes_linked_list.display_nodes()

    print('\nRemoving duplicated nodes:')
    remove_duplicate_nodes(duplicated_nodes_linked_list)
    duplicated_nodes_linked_list.display_nodes()
    '''

    
    # Remove all duplicated nodes
    duplicated_nodes_linked_list = LinkedList()
    duplicated_nodes_linked_list.add_node_in_tail(1)
    duplicated_nodes_linked_list.add_node_in_tail(1)
    duplicated_nodes_linked_list.add_node_in_tail(2)
    duplicated_nodes_linked_list.add_node_in_tail(3)
    duplicated_nodes_linked_list.add_node_in_tail(3)
    duplicated_nodes_linked_list.add_node_in_tail(4)
    duplicated_nodes_linked_list.add_node_in_tail(5)
    duplicated_nodes_linked_list.add_node_in_tail(5)
    duplicated_nodes_linked_list.add_node_in_tail(5)
    duplicated_nodes_linked_list.display_nodes()
    print('\nRemoving all the duplicated nodes:')
    #remove_all_duplicated_nodes_udemy(duplicated_nodes_linked_list)
    deleteDuplicates(duplicated_nodes_linked_list)  # This function is suitable with an ordered LL
    duplicated_nodes_linked_list.display_nodes()
    

    '''
    # Binary to decimal
    binary_linked_list = LinkedList()
    binary_linked_list.add_node_in_tail(1)
    binary_linked_list.add_node_in_tail(1)
    binary_linked_list.add_node_in_tail(0)
    binary_linked_list.add_node_in_tail(1)
    binary_linked_list.display_nodes()
    print('Decimal number is:', binary_to_decimal(binary_linked_list))
    '''

    '''
    # Partition list
    partitioned_list = LinkedList()
    partitioned_list.add_node_in_tail(5)
    partitioned_list.add_node_in_tail(8)
    partitioned_list.add_node_in_tail(6)
    partitioned_list.add_node_in_tail(2)
    partitioned_list.add_node_in_tail(4)
    partitioned_list.add_node_in_tail(1)
    partitioned_list.add_node_in_tail(9)
    partitioned_list.add_node_in_tail(2)
    partitioned_list.add_node_in_tail(4)
    partitioned_list.add_node_in_tail(6)
    partitioned_list.add_node_in_tail(8)
    partitioned_list.add_node_in_tail(3)
    partitioned_list.display_nodes()

    print('Partitioning the list:')
    threshold = 5
    partitioned_list._head = partition_list(partitioned_list, threshold)
    partitioned_list.display_nodes()
    '''

    '''
    # Reverse list
    my_even_linked_list.display_nodes()
    reverse_list(my_even_linked_list)
    #reverse_list_udemy(my_even_linked_list)
    my_even_linked_list.display_nodes()

    my_odd_linked_list.display_nodes()
    reverse_list(my_odd_linked_list)
    #reverse_list_udemy(my_odd_linked_list)
    my_odd_linked_list.display_nodes()
    '''

    '''    
    # Reverse between
    my_odd_linked_list.display_nodes()
    print('Reversing between the linked list...')
    start_index = 1
    end_index = 3
    my_odd_linked_list._head = reverse_between(my_odd_linked_list, start_index, end_index)
    my_odd_linked_list.display_nodes()
    '''

    '''
    # Swapping pairs of nodes.
    my_even_linked_list.display_nodes()
    print('Swapping the nodes in pairs...')
    my_even_linked_list._head = swap_node_pairs(my_even_linked_list)
    my_even_linked_list.display_nodes()

    my_odd_linked_list.display_nodes()
    print('Swapping the nodes in pairs...')
    my_odd_linked_list._head = swap_node_pairs(my_odd_linked_list)
    my_odd_linked_list.display_nodes()
    '''

    '''
    # Interception node
    intercepting_list = LinkedList()
    intercepting_list.add_node_in_tail(4)
    intercepting_list.add_node_in_tail(1)

    intercepted_list = LinkedList()
    intercepted_list.add_node_in_tail(5)
    intercepted_list.add_node_in_tail(6)
    intercepted_list.add_node_in_tail(1)
    intercepted_list.add_node_in_tail(8)
    intercepted_list.add_node_in_tail(4)
    intercepted_list.add_node_in_tail(5)

    index_to_intercept = 3
    list_interceptor(intercepted_list, intercepting_list, index_to_intercept)
    node = intersectionNode_TwoPointers(intercepting_list, intercepted_list)
    print('Intercepting node:', node._value)

    intercepting_list.display_nodes()
    intercepted_list.display_nodes()
    '''

    '''
    # Palindrome
    palindrome_list = LinkedList()
    palindrome_list.add_node_in_tail(1)
    palindrome_list.add_node_in_tail(2)
    palindrome_list.add_node_in_tail(2)
    palindrome_list.add_node_in_tail(1)
    palindrome_list.display_nodes()
    print('is palindrome:', isPalindrome(palindrome_list))

    not_palindrome_list = LinkedList()
    not_palindrome_list.add_node_in_tail(1)
    not_palindrome_list.add_node_in_tail(2)
    not_palindrome_list.add_node_in_tail(1)
    not_palindrome_list.add_node_in_tail(2)
    not_palindrome_list.display_nodes()
    print('is palindrome:', isPalindrome(not_palindrome_list))
    '''

    '''
    # Merge two lists
    list_one = LinkedList()
    list_one.add_node_in_tail(1)
    list_one.add_node_in_tail(2)
    list_one.add_node_in_tail(4)
    list_one.display_nodes()

    list_two = LinkedList()
    list_two.add_node_in_tail(1)
    list_two.add_node_in_tail(3)
    list_two.add_node_in_tail(4)
    list_two.display_nodes()

    merged_list = LinkedList()
    merged_list._head = mergeTwoLists(list_one, list_two)
    merged_list.display_nodes()
    '''

    '''
    #Delete N nodes after M nodes
    my_odd_linked_list.display_nodes()
    my_odd_linked_list._head = deleteNnodesAfterMnodes(my_odd_linked_list, 2, 3)
    my_odd_linked_list.display_nodes()
    '''

    '''
    # Frequency Linked List:
    frequency_linked_list = LinkedList()
    frequency_linked_list.add_node_in_tail(1)
    frequency_linked_list.add_node_in_tail(1)
    frequency_linked_list.add_node_in_tail(2)
    frequency_linked_list.add_node_in_tail(1)
    frequency_linked_list.add_node_in_tail(2)
    frequency_linked_list.add_node_in_tail(3)
    frequency_linked_list.display_nodes()

    frequency_linked_list._head = linkedListFrequency(frequency_linked_list)
    frequency_linked_list.display_nodes()
    '''

    '''
    # Add Two Numbers
    number_one_list = LinkedList()
    number_one_list.add_node_in_head(3)
    number_one_list.add_node_in_head(4)
    number_one_list.add_node_in_head(2)
    number_one_list.display_nodes()

    number_two_list = LinkedList()
    number_two_list.add_node_in_head(4)
    number_two_list.add_node_in_head(6)
    number_two_list.add_node_in_head(5)
    number_two_list.display_nodes()

    sum_list = LinkedList()
    sum_list._head = addTwoNumbers(number_one_list, number_two_list)
    sum_list.display_nodes()
    print()
    number_one_list = LinkedList()
    number_one_list.add_node_in_head(9)
    number_one_list.add_node_in_head(9)
    number_one_list.add_node_in_head(9)
    number_one_list.add_node_in_head(9)
    number_one_list.add_node_in_head(9)
    number_one_list.add_node_in_head(9)
    number_one_list.add_node_in_head(9)
    number_one_list.display_nodes()

    number_two_list = LinkedList()
    number_two_list.add_node_in_head(9)
    number_two_list.add_node_in_head(9)
    number_two_list.add_node_in_head(9)
    number_two_list.add_node_in_head(9)
    number_two_list.display_nodes()

    sum_list = LinkedList()
    sum_list._head = addTwoNumbers(number_one_list, number_two_list)
    sum_list.display_nodes()
    print()
    number_one_list = LinkedList()
    number_one_list.add_node_in_head(1)
    number_one_list.add_node_in_head(9)
    number_one_list.add_node_in_head(9)
    number_one_list.display_nodes()

    number_two_list = LinkedList()
    number_two_list.add_node_in_head(1)
    number_two_list.display_nodes()

    sum_list = LinkedList()
    sum_list._head = addTwoNumbers(number_one_list, number_two_list)
    sum_list.display_nodes()
    '''

    '''
    # Rotate list
    rotates_number = 12
    #my_even_linked_list._head = rotateList(my_even_linked_list, rotates_number)
    my_even_linked_list._head = rotateList_cyclying(my_even_linked_list, rotates_number)
    my_even_linked_list.display_nodes()
    
    my_odd_linked_list.display_nodes()
    rotates_number = 12
    my_odd_linked_list._head = rotateList(my_odd_linked_list, rotates_number)
    #my_odd_linked_list._head = rotateList_cyclying(my_odd_linked_list, rotates_number)
    my_odd_linked_list.display_nodes()
    '''

    '''
    # Reorder List
    my_odd_linked_list.display_nodes()
    print('Reordering list...')
    reorderList(my_odd_linked_list)
    my_odd_linked_list.display_nodes()
    print()
    my_even_linked_list.display_nodes()
    print('Reordering list...')
    reorderList(my_even_linked_list)
    my_even_linked_list.display_nodes()
    '''

    '''
    # PlusOneLinkedList
    plusOneList = LinkedList()
    plusOneList.add_node_in_tail(1)
    plusOneList.add_node_in_tail(9)
    plusOneList.add_node_in_tail(2)
    plusOneList.add_node_in_tail(9)
    plusOneList.display_nodes()
    plusOneLinkedList(plusOneList)
    plusOneList.display_nodes()
    print()
    plusOneListTwo = LinkedList()
    plusOneListTwo.add_node_in_tail(1)
    plusOneListTwo.add_node_in_tail(9)
    plusOneListTwo.add_node_in_tail(2)
    plusOneListTwo.add_node_in_tail(8)
    plusOneListTwo.display_nodes()
    plusOneLinkedList(plusOneListTwo)
    plusOneListTwo.display_nodes()
    print()
    plusOneListThree = LinkedList()
    plusOneListThree.add_node_in_tail(1)
    plusOneListThree.add_node_in_tail(9)
    plusOneListThree.add_node_in_tail(9)
    plusOneListThree.add_node_in_tail(9)
    plusOneListThree.display_nodes()
    plusOneLinkedList(plusOneListThree)
    plusOneListThree.display_nodes()
    print()
    plusOneListFour = LinkedList()
    plusOneListFour.add_node_in_tail(9)
    plusOneListFour.add_node_in_tail(9)
    plusOneListFour.add_node_in_tail(9)
    plusOneListFour.add_node_in_tail(9)
    plusOneListFour.display_nodes()
    plusOneLinkedList(plusOneListFour)
    plusOneListFour.display_nodes()
    '''

    '''
    # Add Two Numbers II
    number_one = LinkedList()
    number_one.add_node_in_tail(9)
    number_one.add_node_in_tail(9)
    number_one.add_node_in_tail(8)
    number_one.add_node_in_tail(5)
    number_one.display_nodes()

    number_two = LinkedList()
    number_two.add_node_in_tail(1)
    number_two.add_node_in_tail(3)
    number_two.add_node_in_tail(5)
    number_two.display_nodes()
    
    result = LinkedList()
    result._head = addTwoNumbersII_no_reverse_two_pointers(number_one, number_two)
    result.display_nodes()
    '''

    '''
    # SplitListInParts
    my_even_linked_list.display_nodes()
    parts_number = 3

    for head in splitListToParts(my_even_linked_list, parts_number):
        list = LinkedList()
        curr = head
        while curr:
            list.add_node_in_tail(curr._value)
            curr = curr._next
        list.display_nodes()

    splitList = LinkedList()
    splitList.add_node_in_tail(1)
    splitList.add_node_in_tail(2)
    splitList.add_node_in_tail(3)
    splitList.display_nodes()
    parts_number = 5

    for head in splitListToParts(splitList, parts_number):
        head
        while head:
            print('head:',head._value)
            head = head._next
    '''

    '''
    # Remove 0 from sublists
    zero_sum_list = LinkedList()
    zero_sum_list.add_node_in_tail(1)
    zero_sum_list.add_node_in_tail(2)
    zero_sum_list.add_node_in_tail(-3)
    zero_sum_list.add_node_in_tail(3)
    zero_sum_list.add_node_in_tail(1)
    zero_sum_list.display_nodes()
    zero_sum_list._head = removeZeroSumSublists(zero_sum_list)
    zero_sum_list.display_nodes()
    print()
    zero_sum_list_two = LinkedList()
    zero_sum_list_two.add_node_in_tail(1)
    zero_sum_list_two.add_node_in_tail(-1)
    zero_sum_list_two.display_nodes()
    zero_sum_list_two._head = removeZeroSumSublists(zero_sum_list_two)
    zero_sum_list_two.display_nodes()
    print()
    zero_sum_list_three = LinkedList()
    zero_sum_list_three.add_node_in_tail(5)
    zero_sum_list_three.add_node_in_tail(-3)
    zero_sum_list_three.add_node_in_tail(-4)
    zero_sum_list_three.add_node_in_tail(1)
    zero_sum_list_three.add_node_in_tail(6)
    zero_sum_list_three.add_node_in_tail(-2)
    zero_sum_list_three.add_node_in_tail(-5)
    zero_sum_list_three.display_nodes()
    zero_sum_list_three._head = removeZeroSumSublists(zero_sum_list_three)
    zero_sum_list_three.display_nodes()
    '''

    '''
    # MergeInBetween
    mergeList = LinkedList()
    mergeList.add_node_in_tail(10)
    mergeList.add_node_in_tail(1)
    mergeList.add_node_in_tail(13)
    mergeList.add_node_in_tail(6)
    mergeList.add_node_in_tail(9)
    mergeList.add_node_in_tail(5)
    mergeList.display_nodes()

    mergingList = LinkedList()
    mergingList.add_node_in_tail(1000000)
    mergingList.add_node_in_tail(1000001)
    mergingList.add_node_in_tail(1000002)
    mergingList.display_nodes()

    start_node = 3
    end_node = 4
    mergeList._head = mergeInBetween(mergeList, start_node, end_node, mergingList)
    mergeList.display_nodes()
    '''

    '''
    # Swap nodes
    
    my_odd_linked_list.display_nodes()
    my_odd_linked_list._head = swapNodes(my_odd_linked_list, 2)
    my_odd_linked_list.display_nodes()

    swap_list = LinkedList()
    swap_list.add_node_in_tail(100)
    swap_list.add_node_in_tail(90)
    swap_list.display_nodes()
    swap_list._head = swapNodes(swap_list, 2)
    swap_list.display_nodes()
    '''

    '''
    # Nodes between critical points
    critical_point_list = LinkedList()
    critical_point_list.add_node_in_tail(5)
    critical_point_list.add_node_in_tail(3)
    critical_point_list.add_node_in_tail(1)
    critical_point_list.add_node_in_tail(2)
    critical_point_list.add_node_in_tail(5)
    critical_point_list.add_node_in_tail(1)
    critical_point_list.add_node_in_tail(2)
    critical_point_list.display_nodes()
    print(nodesBetweenCriticalPoints(critical_point_list))
    
    critical_point_list_two = LinkedList()
    critical_point_list_two.add_node_in_tail(2)
    critical_point_list_two.add_node_in_tail(2)
    critical_point_list_two.add_node_in_tail(1)
    critical_point_list_two.add_node_in_tail(3)
    critical_point_list_two.display_nodes()
    print(nodesBetweenCriticalPoints(critical_point_list_two))
    '''

    '''
    # Reverse Even Length groups
    even_length_list = LinkedList()
    even_length_list.add_node_in_tail(5)
    even_length_list.add_node_in_tail(2)
    even_length_list.add_node_in_tail(6)
    even_length_list.add_node_in_tail(3)
    even_length_list.add_node_in_tail(9)
    even_length_list.add_node_in_tail(1)
    even_length_list.add_node_in_tail(7)
    even_length_list.add_node_in_tail(3)
    even_length_list.add_node_in_tail(8)
    even_length_list.add_node_in_tail(4)
    even_length_list.display_nodes()
    even_length_list._head = reverseEvenLengthGroups(even_length_list)
    even_length_list.display_nodes()
    
    even_length_list_two = LinkedList()
    even_length_list_two.add_node_in_tail(1)
    even_length_list_two.add_node_in_tail(1)
    even_length_list_two.add_node_in_tail(0)
    even_length_list_two.add_node_in_tail(6)
    even_length_list_two.add_node_in_tail(5)
    even_length_list_two.display_nodes()
    even_length_list_two._head = reverseEvenLengthGroups(even_length_list_two)
    even_length_list_two.display_nodes()
    '''

    '''
    # Spiral matrix
    spiral_list = LinkedList()
    spiral_list.add_node_in_tail(3)
    spiral_list.add_node_in_tail(0)
    spiral_list.add_node_in_tail(2)
    spiral_list.add_node_in_tail(6)
    spiral_list.add_node_in_tail(8)
    spiral_list.add_node_in_tail(1)
    spiral_list.add_node_in_tail(7)
    spiral_list.add_node_in_tail(9)
    spiral_list.add_node_in_tail(4)
    spiral_list.add_node_in_tail(2)
    spiral_list.add_node_in_tail(5)
    spiral_list.add_node_in_tail(5)
    spiral_list.add_node_in_tail(0)
    columns = 5
    rows = 3
    spiralMatrix(columns, rows, spiral_list)
    '''

    '''
    # Split a Circular Linked List
    print('\n ---> my_even_linked_list')
    cycle_tail_at_head(my_even_linked_list)
    hasLoopAtNode(my_even_linked_list)
    print(splitCircularLinkedList(my_even_linked_list))
    
    print('\n ---> split_circular_list')
    split_circular_list = LinkedList()
    split_circular_list.add_node_in_tail(1)
    split_circular_list.add_node_in_tail(2)
    split_circular_list.add_node_in_tail(3)
    split_circular_list.add_node_in_tail(4)
    split_circular_list.add_node_in_tail(5)
    cycle_tail_at_head(split_circular_list)
    hasLoopAtNode(split_circular_list)
    print(splitCircularLinkedList(split_circular_list))
    '''

    '''
    # Insert greatest common divisor
    great_common_divisor = LinkedList()
    great_common_divisor.add_node_in_tail(18)
    great_common_divisor.add_node_in_tail(6)
    great_common_divisor.add_node_in_tail(10)
    great_common_divisor.add_node_in_tail(3)
    great_common_divisor.display_nodes()
    great_common_divisor._head = insertGreatestCommonDivisors(great_common_divisor)
    great_common_divisor.display_nodes()
    '''

    '''
    # Delete nodes present in Linked List present in Array
    modified_list = LinkedList()
    for i in range(len(input.a_huge_ll)):
        modified_list.add_node_in_tail(input.a_huge_ll[i])
    modified_list.display_nodes()
    modified_list._head = modifiedList(input.nums, modified_list)
    modified_list.display_nodes()
    '''
    
    '''
    modified_list_two = LinkedList()
    modified_list_two.add_node_in_tail(1)
    modified_list_two.add_node_in_tail(2)
    modified_list_two.add_node_in_tail(3)
    modified_list_two.add_node_in_tail(4)
    modified_list_two.add_node_in_tail(5)
    modified_list_two.display_nodes()
    nums = [1, 2, 3]
    modified_list_two._head = modifiedList(nums, modified_list_two)
    modified_list_two.display_nodes()
    '''
