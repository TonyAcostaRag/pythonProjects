# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# First 
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        initial = head
        pointer = head
        counter = 0
        while pointer is not None:
            pointer = pointer.next
            counter += 1

        point_tracker = [0] * counter
        counter = 0
        pointer = initial

        while pointer is not None:

            if point_tracker[pointer.val] != 0:
                return counter
            point_tracker.insert(pointer.val, pointer.val)
            pointer = pointer.next

        return None


# Second

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        point_tracker = []
        pointer = head

        while pointer is not None:
            print(pointer.val)
            
            if pointer.val in point_tracker:
                return pointer
            else:
                point_tracker.append(pointer.val)
                pointer = pointer.next

        return pointer
    

    # Third

    # Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast_pointer = head
        slow_pointer = head
        counter = 0

        while fast_pointer.next is not None and fast_pointer is not None:
            counter += 1
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
            print('fast:', fast_pointer.val)
            print('slow:', slow_pointer.val)
            print('counter:', counter)

            if fast_pointer.val == slow_pointer.val:
                return slow_pointer



        return None
