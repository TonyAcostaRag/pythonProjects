from dataStructures.Linear.queue.QueueLinked import QueueLinked
from dataStructures.Graphs.VertexList.VertexList import VertexListed


class breadth_first_search:

    def traverse(self, root):
        q = QueueLinked()
        q.enqueue(root)
        root.setVisited()

        while not q.is_empty():

            actualVertex = q.dequeue()
            print('On Vertex:', actualVertex)
            for neighbor in actualVertex.get_adjacency_list():
                if not neighbor.isVisited():
                    neighbor.setVisited()
                    q.enqueue(neighbor)


if __name__ == '__main__':
    bfs = breadth_first_search()

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

    bfs.traverse(a)
