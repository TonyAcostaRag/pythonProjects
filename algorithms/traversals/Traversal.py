class Traversal:

    def __init__(self, data_structure):
        self._ds = data_structure()

    def traverse(self, cluster_list):

        for vertex in cluster_list:
            if not vertex.isVisited():
                self._ds.enter_element(vertex)
                vertex.setVisited()

                while not self._ds.is_empty():

                    actual_vertex = self._ds.take_out_element()
                    print('On Vertex:', actual_vertex)
                    for neighbor in actual_vertex.get_adjacency_list():
                        if not neighbor.isVisited():
                            neighbor.setVisited()
                            self._ds.enter_element(neighbor)
