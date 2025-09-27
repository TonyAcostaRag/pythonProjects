class Graph:
    
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list and v1 in self.adj_list[v2] and v2 in self.adj_list[v1]:
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex not in self.adj_list:
            return False
        
        for v in self.adj_list[vertex]:
            self.adj_list[v].remove(vertex)

        del self.adj_list[vertex]
        return True
    
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])


if __name__ == '__main__':

    my_graph = Graph()
    my_graph.add_vertex('A')
    my_graph.add_vertex('B')
    my_graph.add_vertex('C')
    my_graph.add_vertex('D')

    my_graph.add_edge('A', 'B')
    my_graph.add_edge('C', 'A')
    my_graph.add_edge('C', 'D')
    my_graph.add_edge('B', 'D')
    my_graph.add_edge('A', 'D')
    
    my_graph.print_graph()

    my_graph.remove_vertex('D')

    my_graph.print_graph()
