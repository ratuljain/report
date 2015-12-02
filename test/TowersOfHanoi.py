from collections import deque
graph = {'A': set(['B', 'C']),
'B': set(['A', 'D', 'E']),
'C': set(['A', 'F']),
'D': set(['B']),
'E': set(['B', 'F']),
'F': set(['C', 'E'])}

g = {'A': ['B', 'D', 'G'],
'B': ['A', 'E', 'F'],
'C': ['F', 'H'],
'D': ['A', 'F'],
'E': ['B', 'G'],
'F': ['B', 'C', 'D'],
'G': ['A', 'E'],
'H': ['C']
}

def dfs(graph, start):
    visited = []
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
        rem = [x for x in graph[vertex] if x not in visited]
        stack.extend(rem[::-1])
    return visited

def bfs(graph, start):
    visited = []
    queue = deque([(start)])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.append(vertex)
        rem = [x for x in graph[vertex] if x not in visited]
        queue.extend(rem)
    return visited

print dfs(g, 'A')
print bfs(g, 'A')