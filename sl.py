from collections import deque

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
    return -1  # or raise appropriate exception
def depth_first(g,s,d):
    dist={}
    queue=deque([s])
    ob=[s]
    sp=1
    dist[s]=sp
    while True:
        node=queue.popleft()
        if d in g[node]:
            return dist[node]
        else:
            for neighbour in g[node]:
                if neighbour not in ob:
                    dist[neighbour]=dist[node]+1
                    queue.append(neighbour)
                    ob.append(neighbour)


graph = {}
l = []
s = []
l.extend(s)
for i in range(1, 95):
    graph[i] = range(i + 1, i + 7)
for i in range(95, 100):
    graph[i] = range(i + 1, 101)

for t in l:
    del graph[t[0]]
    for i in range(max(0, t[0] - 6), t[0]):
        if i in graph:
            graph[i].remove(t[0])
            graph[i].append(t[1])

print len(shortest_path(graph, 1, 100)) - 1
