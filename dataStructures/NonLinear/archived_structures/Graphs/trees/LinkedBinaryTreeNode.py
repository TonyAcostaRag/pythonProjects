class LinkedBinaryTreeNode:

    def __init__(self, element, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right
        self._is_visited = False

    def add_children(self, left, right):
        self._left = left
        self._right = right

    def get_children(self):
        if self._left is None and self._right is None:
            return []
        return [self._left, self._right]

    def set_visited(self):
        self._is_visited = True

    def is_visited(self):
        return self._is_visited

    def __str__(self):
        return str(self._element)


if __name__ == '__main__':
    a = LinkedBinaryTreeNode('A')
    b = LinkedBinaryTreeNode('B')
    c = LinkedBinaryTreeNode('C')
    d = LinkedBinaryTreeNode('D')
    e = LinkedBinaryTreeNode('E')
    f = LinkedBinaryTreeNode('F')
    g = LinkedBinaryTreeNode('G')

    a.add_children(b, c)
    b.add_children(d, e)
    c.add_children(f, g)

    for node in [a, b, c]:
        if len(a.get_children()) > 0:
            for child in node.get_children():
                print(child, ' is child of', node)
            print()
