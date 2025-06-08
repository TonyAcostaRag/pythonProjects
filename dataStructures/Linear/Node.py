class _Node:
    __slots__ = '_value', '_next'

    def __init__(self, value):
        self._value = value
        self._next = None


if __name__ == '__main__':

    node_one = _Node(1)

    node_two = _Node(2)
    node_one._next = node_two

    node_three = _Node(3)
    node_two._next = node_three

    print(node_one._value)
    print(node_one._next._value)
    print(node_one._next._next._value)
    print(node_one._next._next._next)
