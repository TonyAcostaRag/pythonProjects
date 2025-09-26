class Node:
    __slots__ = 'value', 'next'

    def __init__(self, value):
        self.value = value
        self.next = None


class DualNode:
    __slots__ = 'value', 'next', 'prev'

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class TreeNode:
    __slots__ = 'value', 'left', 'right'

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


if __name__ == '__main__':

    node_one = Node(1)

    node_two = Node(2)
    node_one.next = node_two

    node_three = Node(3)
    node_two.next = node_three

    print(node_one.value)
    print(node_one.next.value)
    print(node_one.next.next.value)
    print(node_one.next.next.next)
