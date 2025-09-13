from dataStructures.Linear.Node import _Node
from dataStructures.Linear.LinkedList.LinkedList import LinkedList


class MyHashSet:

    def __init__(self):
        self.buckets = [LinkedList() for _ in range(10)]

    def add(self, key: int) -> None:

        current = self.buckets[key % 10]._head
        if current is None:
            self.buckets[key % 10]._head = _Node(key)
        else:
            while True:
                if current._value == key:
                    return

                if current._next is None:
                    current._next = _Node(key)
                    return
                current = current._next

    def remove(self, key: int) -> None:
        dummy_node = _Node(None)
        dummy_node._next = self.buckets[key % 10]._head
        current = dummy_node
        while current and current._next:

            if current._next._value == key:
                current._next = current._next._next
                break
            current = current._next

    def contains(self, key: int) -> bool:
        current = self.buckets[key % 10]._head
        while current:
            if current._value == key:
                return True
            current = current._next
        return False
        
    def display_values_in_buckets(self):
        print('\nDisplaying the Hash Set content:')
        for i in range(len(self.buckets)):
            current = self.buckets[i]._head
            print(i, ':', end=' ')
            while current:
                print(current._value, end=' ')
                if current._next:
                    print('->', end=' ')
                current = current._next
            print()
        

if __name__ == '__main__':

    my_hash_set = MyHashSet()
    my_hash_set.add(9)
    my_hash_set.add(8)
    my_hash_set.add(7)
    my_hash_set.add(6)
    my_hash_set.add(5)
    '''
    my_hash_set.add(4)
    my_hash_set.add(3)
    my_hash_set.add(2)
    my_hash_set.add(1)
    my_hash_set.add(10)
    '''

    print('\nDisplaying items within HashSet:')
    my_hash_set.display_values_in_buckets()

    print('\nChecking if hashset contain values:')
    print(my_hash_set.contains(8))
    print(my_hash_set.contains(1))

    print('\nDeleting existing values:')
    my_hash_set.remove(8)

    print('\nChecking if hashset contain values:')
    print(my_hash_set.contains(8))
    print(my_hash_set.contains(1))

    print('\nTrying to Delete non-existing values:')
    my_hash_set.remove(1)

    print('\nCollisions handling:')
    my_hash_set.add(9)
    my_hash_set.add(19)
    my_hash_set.add(29)
    my_hash_set.add(9)
    my_hash_set.add(19)
    my_hash_set.add(99)
    my_hash_set.add(39)
    print(my_hash_set.contains(9))
    print(my_hash_set.contains(19))
    my_hash_set.display_values_in_buckets()
    print('Deleting 99')
    my_hash_set.remove(99)
    my_hash_set.display_values_in_buckets()
    my_hash_set.remove(99)
    print(my_hash_set.contains(39))
    print(my_hash_set.contains(99))

    my_hash_set.add(11)
    my_hash_set.add(44)
    my_hash_set.add(87)
    my_hash_set.add(64)
    my_hash_set.add(66)
    my_hash_set.add(51)
    my_hash_set.add(91)
    my_hash_set.add(80)
    my_hash_set.add(16)
    my_hash_set.add(16)
    my_hash_set.add(22)
    my_hash_set.add(22)
    my_hash_set.display_values_in_buckets()
