class VertexListed:

    def __init__(self, name):
        self._name = name
        self._isVisited = False
        self._adjacencyList = []

    def setVisited(self):
        self._isVisited = True

    def isVisited(self):
        return self._isVisited

    def get_adjacency_list(self):
        return self._adjacencyList

    def add_neighbor(self, vertex):
        self._adjacencyList.append(vertex)

    def __str__(self):
        return str(self._name)


if __name__ == '__main__':
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

    for vertex in [a, b, c, d, e, f, g, h]:
        if len(vertex.get_adjacency_list()) > 0:
            for neighbor in vertex.get_adjacency_list():
                print('Vertex', vertex, 'Has the neighbors:', neighbor)
            print()
