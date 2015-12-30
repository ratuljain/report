from collections import deque


def init():
    graph = {}
    for i in range(1, 95):
        graph[i] = range(i + 1, i + 7)
    for i in range(95, 100):
        graph[i] = range(i + 1, 101)
    return graph


def bfs(g, start):
    queue, enqueued = deque([(None, start)]), set([start])
    while queue:
        parent, n = queue.popleft()
        yield parent, n
        new = set(g[n]) - enqueued
        enqueued |= new
        queue.extend([(n, child) for child in new])


def shortest_path(g, start, end):
    parents = {}
    for parent, child in bfs(g, start):
        parents[child] = parent
        if child == end:
            revpath = [end]
            while True:
                parent = parents[child]
                revpath.append(parent)
                if parent == start:
                    break
                child = parent
            return list(reversed(revpath))
    return -1


def minMoves():
    graph = init()
    ladders = []
    snakes = []
    l = int(raw_input())
    for i in xrange(l):
        ladders.append(tuple([int(i) for i in raw_input().split(" ")]))

    s = int(raw_input())
    for i in xrange(s):
        snakes.append(tuple([int(i) for i in raw_input().split(" ")]))
    ladders.extend(snakes)
    for t in ladders:
        del graph[t[0]]
        for i in range(max(0, t[0] - 6), t[0]):
            if i in graph:
                graph[i].remove(t[0])
                graph[i].append(t[1])
    if shortest_path(graph, 1, 100) == -1:
        print -1
        return
    print len(shortest_path(graph, 1, 100)) - 1


for i in range(input()):
    minMoves()
