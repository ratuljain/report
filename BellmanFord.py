__author__ = 'rjain1'
graph = {
    'A': {'B': 8, 'E': 6},
    'B': {'C': 6},
    'C': {'H': 4},
    'D': {'B': 2},
    'E': {'F': 3, 'G': 2},
    'F': {'G': 6},
    'G': {'C': -1, 'D': 1},
    'H': {'G': -2}
}


def relax(node, neighbour, graph, distance, predecessor):
    if distance[neighbour] > distance[node] + graph[node][neighbour]:
        distance[neighbour] = distance[node] + graph[node][neighbour]
        predecessor[neighbour] = node


def bellman_ford(graph, start):
    distance = {node: float('inf') for node in graph}
    predecessor = {node: None for node in graph}
    distance[start] = 0
    for i in range(len(graph) - 1):
        for u in graph:
            for v in graph[u]:
                relax(u, v, graph, distance, predecessor)

    for u in graph:
        for v in graph[u]:
            if distance[v] > distance[u] + graph[u][v]:
                return "Graph has negative weights"

    return distance, predecessor


# print bellman_ford(graph)

def test():
    graph = {
        'a': {'b': -1, 'c': 4},
        'b': {'c': 3, 'd': 2, 'e': 2},
        'c': {},
        'd': {'b': 1, 'c': 5},
        'e': {'d': -3}
    }

    d, p = bellman_ford(graph, 'a')

    assert d == {
        'a': 0,
        'b': -1,
        'c': 2,
        'd': -2,
        'e': 1
    }

    assert p == {
        'a': None,
        'b': 'a',
        'c': 'b',
        'd': 'e',
        'e': 'b'
    }


test()
