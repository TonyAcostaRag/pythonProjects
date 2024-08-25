from dataStructures.Linear.stack.StackLinked import StackLinked
from dataStructures.NonLinear.Graphs.VertexList.VertexList import VertexListed
from algorithms.traversals.Traversal import Traversal


class DepthFirstSearch(Traversal):

    def __init__(self):
        self.stack = StackLinked
        super().__init__(self.stack)


if __name__ == '__main__':

    dfs = DepthFirstSearch()

    a = VertexListed('A')
    b = VertexListed('B')
    c = VertexListed('C')
    d = VertexListed('D')
    e = VertexListed('E')

    a.add_neighbor(b)
    a.add_neighbor(c)

    c.add_neighbor(d)

    d.add_neighbor(e)

    dfs.traverse([a, b, c, d, e])

    a = VertexListed('A')
    b = VertexListed('B')
    c = VertexListed('C')
    d = VertexListed('D')
    e = VertexListed('E')
    f = VertexListed('F')
    g = VertexListed('G')
    h = VertexListed('H')

    a.add_neighbor(b)
    a.add_neighbor(f)
    a.add_neighbor(g)

    b.add_neighbor(c)
    b.add_neighbor(d)

    g.add_neighbor(h)

    d.add_neighbor(e)

    dfs.traverse([a, b, c, d, e, f, g, h])
