__author__ = 'rjain1'
class Graph():
    def __init__(self, graph_dict={}):
        self.graph = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.graph.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, edge):
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.graph[vertex1].append(vertex2)
        else:
            self.graph[vertex1] = [vertex2]

    def __generate_edges(self):
        edges = []
        for vertex in self.graph:
            for neighbour in self.graph[vertex]:
                if (neighbour, vertex) not in edges:
                    edges.append((vertex, neighbour))
        return edges

class UnionFind():
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0 for i in range(n)]

    def find(self, v):
        if not v == self.parent[v]:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot == yRoot:
            return
        if self.rank[xRoot] > self.rank[yRoot]:
            self.parent[yRoot] = xRoot
        else:
            self.parent[xRoot] = yRoot
            if self.rank[xRoot] == self.rank[yRoot]:
                self.rank[yRoot] += 1

    def printParent(self):
        print("index: ",list(range(3)))
        print("parent: ", self.parent)


g = {0: [1, 2],
     1: [0, 2],
     2: [0, 1]}
graph = Graph(g)
print graph.vertices()
res = UnionFind(len(graph.vertices()))
res.union(0,1)
print res.printParent()
print graph.edges()

