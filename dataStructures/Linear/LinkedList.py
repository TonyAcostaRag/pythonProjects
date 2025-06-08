from dataStructures.Linear.Node import _Node


class LinkedList:
    __slots__ = '_head', '_tail', '_size'

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def get_head(self):
        if self._head is None:
            return self._head
        else:
            return self._head._value

    def get_tail(self):
        if self._tail is None:
            return self._tail
        else:
            return self._tail._value

    def get_size(self):
        return self._size

    def add_node_in_tail(self, node):
        new_node = _Node(node)
        if self._size == 0:
            self._head = new_node
        else:
            self._tail._next = new_node
        self._size += 1
        self._tail = new_node

    def add_node_in_head(self, node):
        new_node = _Node(node)
        if self._size == 0:
            self._tail = new_node
        else:
            new_node._next = self._head
        self._size += 1
        self._head = new_node

    def add_node_at_index(self, node, index_to_insert):
        if self._size == 0 or index_to_insert == 0:
            self.add_node_in_head(node)
        elif index_to_insert < self._size - 1:
            new_node = _Node(node)
            index = 1
            pointer = self._head
            while index < index_to_insert:
                index += 1
                pointer = pointer._next
            new_node._next = pointer._next
            pointer._next = new_node
            self._size += 1
        else:
            self.add_node_in_tail(node)

    def delete_head(self):
        if self._size == 0:
            return
        node_removed = self._head._value
        self._head = self._head._next
        self._size -= 1
        if self._size == 0:
            self._tail = None
        return node_removed

    def delete_tail(self):
        if self._size == 0:
            return
        elif self._size == 1:
            removed_node = self._tail._value
            self._head = None
            self._tail = None
        else:
            index = 0
            pointer = self._head
            while index < self._size - 2:
                index += 1
                pointer = pointer._next
            removed_node = pointer._next._value
            self._tail = pointer
            self._tail._next = None
        self._size -= 1
        return removed_node

    def delete_node_at_index(self, index_to_delete):
        if self._size == 0 or index_to_delete > self._size:
            return
        if index_to_delete == 0:
            self.delete_head()
        elif index_to_delete < self._size - 1:
            pointer = self._head
            index = 1
            while index < index_to_delete:
                index += 1
                pointer = pointer._next
            deleted_node = pointer._next._value
            pointer._next = pointer._next._next
            self._size -= 1
            return deleted_node
        else:
            self.delete_tail()

    def search_node(self, key):
        pointer = self._head
        index_node = 0
        while pointer:
            if pointer._value == key:
                return index_node
            pointer = pointer._next
            index_node += 1
        return -1

    def inserted_sorted(self, node):
        new_node = _Node(node)
        if self._size == 0:
            self._head = new_node
        else:
            pointer = self._head
            temp = self._head
            while pointer and pointer._value < node:
                temp = pointer
                pointer = pointer._next
            if pointer == self._head:
                new_node._next = self._head
                self._head = new_node
            else:
                new_node._next = temp._next
                temp._next = new_node
        self._size += 1

    def display_nodes(self):
        pointer = self._head
        while pointer:
            print(pointer._value, end=' --> ')
            pointer = pointer._next
        if self._tail is None:
            print(self._tail)
        else:
            print(self._tail._next)


if __name__ == '__main__':

    linked_List = LinkedList()
    linked_List.add_node_in_tail(1)
    linked_List.add_node_in_tail(2)
    linked_List.add_node_in_tail(3)
    linked_List.add_node_in_tail(4)
    linked_List.add_node_in_tail(5)
    linked_List.add_node_in_tail(6)

    print('Linked List:', end=' ')
    linked_List.display_nodes()
    print('Head:', linked_List.get_head())
    print('Tail:',linked_List.get_tail())
    print('Next node after head:', linked_List._head._next._value)
    print('Next node after tail:', linked_List._tail._next)
    print('List Size:', linked_List.get_size())

    print()

    linked_List_Line_Mgmt = LinkedList()
    linked_List_Line_Mgmt.add_node_in_tail('Arvind')
    linked_List_Line_Mgmt.add_node_in_tail('Ann Funai')
    linked_List_Line_Mgmt.add_node_in_tail('Managers')
    linked_List_Line_Mgmt.add_node_in_tail('Dev Team')

    print('Linked List:', end=' ')
    linked_List_Line_Mgmt.display_nodes()
    print('Head:', linked_List_Line_Mgmt.get_head())
    print('Tail:',linked_List_Line_Mgmt.get_tail())
    print('Next node after head:', linked_List_Line_Mgmt._head._next._value)
    print('Next node after tail:', linked_List_Line_Mgmt._tail._next)
    print('List Size:', linked_List_Line_Mgmt.get_size())
    print('Index of Arvind:', linked_List_Line_Mgmt.search_node('Arvind'))
    print('Index of Ginni:', linked_List_Line_Mgmt.search_node('Ginni'))
    print('Index of Dev Team:', linked_List_Line_Mgmt.search_node('Dev Team'))

    print('\nInserting investors in head')
    linked_List_Line_Mgmt.add_node_in_head('Investors')
    print('Linked List:', end=' ')
    linked_List_Line_Mgmt.display_nodes()
    print('Head:', linked_List_Line_Mgmt.get_head())
    print('Tail:', linked_List_Line_Mgmt.get_tail())
    print('Next node after head:', linked_List_Line_Mgmt._head._next._value)
    print('Next node after tail:', linked_List_Line_Mgmt._tail._next)
    print('List Size:', linked_List_Line_Mgmt.get_size())
    print('Index of Arvind:', linked_List_Line_Mgmt.search_node('Arvind'))
    print('Index of Ginni:', linked_List_Line_Mgmt.search_node('Ginni'))
    print('Index of Dev Team:', linked_List_Line_Mgmt.search_node('Dev Team'))

    print('\nInserting Cesare at index 3')
    linked_List_Line_Mgmt.add_node_at_index('Cesare', 3)
    print('Linked List:', end=' ')
    linked_List_Line_Mgmt.display_nodes()
    print('Head:', linked_List_Line_Mgmt.get_head())
    print('Tail:', linked_List_Line_Mgmt.get_tail())
    print('Next node after head:', linked_List_Line_Mgmt._head._next._value)
    print('Next node after tail:', linked_List_Line_Mgmt._tail._next)
    print('List Size:', linked_List_Line_Mgmt.get_size())
    print('Index of Arvind:', linked_List_Line_Mgmt.search_node('Arvind'))
    print('Index of Ginni:', linked_List_Line_Mgmt.search_node('Ginni'))
    print('Index of Dev Team:', linked_List_Line_Mgmt.search_node('Dev Team'))

    print('\nInserting Mayor Investor at index 0')
    linked_List_Line_Mgmt.add_node_at_index('Mayor Investor', 0)
    print('Linked List:', end=' ')
    linked_List_Line_Mgmt.display_nodes()
    print('Head:', linked_List_Line_Mgmt.get_head())
    print('Tail:', linked_List_Line_Mgmt.get_tail())
    print('Next node after head:', linked_List_Line_Mgmt._head._next._value)
    print('Next node after tail:', linked_List_Line_Mgmt._tail._next)
    print('List Size:', linked_List_Line_Mgmt.get_size())
    print('Index of Arvind:', linked_List_Line_Mgmt.search_node('Arvind'))
    print('Index of Ginni:', linked_List_Line_Mgmt.search_node('Ginni'))
    print('Index of Dev Team:', linked_List_Line_Mgmt.search_node('Dev Team'))

    print('\nInserting Student at last index')
    linked_List_Line_Mgmt.add_node_at_index('Student', linked_List_Line_Mgmt._size-1)
    print('Linked List:', end=' ')
    linked_List_Line_Mgmt.display_nodes()
    print('Head:', linked_List_Line_Mgmt.get_head())
    print('Tail:', linked_List_Line_Mgmt.get_tail())
    print('Next node after head:', linked_List_Line_Mgmt._head._next._value)
    print('Next node after tail:', linked_List_Line_Mgmt._tail._next)
    print('List Size:', linked_List_Line_Mgmt.get_size())
    print('Index of Arvind:', linked_List_Line_Mgmt.search_node('Arvind'))
    print('Index of Ginni:', linked_List_Line_Mgmt.search_node('Ginni'))
    print('Index of Dev Team:', linked_List_Line_Mgmt.search_node('Dev Team'))

    print('\nDeleting the head:')
    print('Removed node:', linked_List_Line_Mgmt.delete_head())
    print('Linked List:', end=' ')
    linked_List_Line_Mgmt.display_nodes()
    print('Head:', linked_List_Line_Mgmt.get_head())
    print('Tail:', linked_List_Line_Mgmt.get_tail())
    print('Next node after head:', linked_List_Line_Mgmt._head._next._value)
    print('Next node after tail:', linked_List_Line_Mgmt._tail._next)
    print('List Size:', linked_List_Line_Mgmt.get_size())
    print('Index of Arvind:', linked_List_Line_Mgmt.search_node('Arvind'))
    print('Index of Ginni:', linked_List_Line_Mgmt.search_node('Ginni'))
    print('Index of Dev Team:', linked_List_Line_Mgmt.search_node('Dev Team'))

    print('\nDeleting head by head:')
    print('Linked List:')
    linked_List.display_nodes()
    linked_List.delete_head()
    linked_List.display_nodes()
    linked_List.delete_head()
    linked_List.display_nodes()
    linked_List.delete_head()
    linked_List.display_nodes()
    linked_List.delete_head()
    linked_List.display_nodes()
    linked_List.delete_head()
    linked_List.display_nodes()
    linked_List.delete_head()
    linked_List.display_nodes()
    linked_List.delete_head()
    linked_List.display_nodes()
    print('Head:', linked_List.get_head())
    print('Tail:', linked_List.get_tail())
    print('List Size:', linked_List.get_size())

    print('\nDeleting tail by tail:')
    linked_List.add_node_in_tail(1)
    linked_List.add_node_in_tail(2)
    linked_List.add_node_in_tail(3)
    linked_List.add_node_in_tail(4)
    linked_List.add_node_in_tail(5)
    linked_List.add_node_in_tail(6)
    print('Linked List:')
    linked_List.display_nodes()
    print('List Size:', linked_List.get_size())
    linked_List.delete_tail()
    linked_List.display_nodes()
    linked_List.delete_tail()
    linked_List.display_nodes()
    linked_List.delete_tail()
    linked_List.display_nodes()
    linked_List.delete_tail()
    linked_List.display_nodes()
    linked_List.delete_tail()
    linked_List.display_nodes()
    linked_List.delete_tail()
    linked_List.display_nodes()
    linked_List.delete_tail()
    linked_List.display_nodes()
    linked_List.delete_tail()
    linked_List.display_nodes()

    print('\nDeleting node by index:')
    linked_List.add_node_in_tail(1)
    linked_List.add_node_in_tail(2)
    linked_List.add_node_in_tail(3)
    linked_List.add_node_in_tail(4)
    linked_List.add_node_in_tail(5)
    linked_List.add_node_in_tail(6)
    print('Linked List:')
    linked_List.display_nodes()
    print('Deleting index 2')
    linked_List.delete_node_at_index(2)
    linked_List.display_nodes()
    print('Deleting index 0')
    linked_List.delete_node_at_index(0)
    linked_List.display_nodes()
    print('Deleting index 3')
    linked_List.delete_node_at_index(3)
    linked_List.display_nodes()
    print('Deleting index 1')
    linked_List.delete_node_at_index(1)
    linked_List.display_nodes()
    print('Deleting index 1')
    linked_List.delete_node_at_index(1)
    linked_List.display_nodes()
    print('Deleting index 0')
    linked_List.delete_node_at_index(0)
    linked_List.display_nodes()
    linked_List.delete_node_at_index(5)
    linked_List.display_nodes()
