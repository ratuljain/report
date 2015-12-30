__author__ = 'rjain1'
g = {0: {1: 6, 2: 8},
     1: {4: 11},
     2: {3: 9},
     3: {},
     4: {5: 3},
     5: {2: 7, 3: 4}}

graph = {
    0: {1: 5, 3: 10},
    1: {2: 3},
    2: {3: 1},
    3: {}
}


def floydwarshall(graph):
    dist = {}
    pred = {}
    for u in graph:
        dist[u] = {}
        pred[u] = {}
        for v in graph:
            dist[u][v] = float('inf')
            pred[u][v] = None
        dist[u][u] = 0
        for neighbor in graph[u]:
            dist[u][neighbor] = graph[u][neighbor]
            pred[u][neighbor] = u

    for k in graph:
        for i in graph:
            for j in graph:
                # if dist[i][k] + dist[k][j] < dist[i][j]:
                #     dist[i][j] = dist[i][k] + dist[k][j]
                #     pred[i][j] = pred[i][k]
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist, pred


dist, pred = floydwarshall(graph)
# print getPath(pred, 0, 3)
# pred = floydwarshall(graph)[1]
# print getPath(pred, 0, 3)


for i in dist:
    print i, dist[i]
for i in pred:
    print i, pred[i]
