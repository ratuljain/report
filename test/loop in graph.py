__author__ = 'rjain1'

distances = {
     0: {1: 4, 7: 8},
     1: {0: 4, 2: 8, 7: 11},
     2: {8: 2, 1: 8, 3: 7, 5: 4},
     3: {2: 7, 4: 9, 5: 14},
     4: {3: 9, 5: 10},
     5: {2: 4, 4: 10, 6: 2},
     6: {8: 6, 3: 14, 5: 2, 7: 1},
     7: {0: 8, 1: 11, 6: 1, 8: 7},
     8: {2: 2, 6: 6, 7: 7}
    }

def dfs(graph, start):
    color = {i : 'white' for i in graph}
    stack = [start]
    visited = []

    while stack:
        vertex = stack.pop()
        if color[vertex] == 'grey':
            return True
        color[vertex] = 'grey'
        visited.append(vertex)
        stack.extend((graph[vertex]))
        if len(graph[vertex]) == 0:
            color[vertex] = 'black'
    return False

def cycle_exists(graph):
    for vertex in graph:
         if(dfs(graph, vertex)):
             return True
    return False

graph1 = { 0 : [1, 2],
           1 : [],
           2 : [3],
           3 : [4],
           4 : [2] }
assert(cycle_exists(graph1) == True)
print("Graph1 has a cycle.")

#----------------------------------------------------

# disconnected graph with cycle
graph2 = { 0 : [],
           1 : [2],
           2 : [],
           3 : [4],
           4 : [5],
           5 : [3] }
assert(cycle_exists(graph2) == True)
print("Graph2 has a cycle.")

#----------------------------------------------------

# disconnected graph without a cycle
graph3 = { 0 : [],
           1 : [],
           2 : [],
           3 : [] }
assert(cycle_exists(graph3) == False)
print("Graph3 has no cycle.")

#----------------------------------------------------

# disconnected graph without a cycle
graph4 = { 0 : [1, 2],
           1 : [3, 4],
           2 : [],
           3 : [],
           4 : [],
           5 : [6, 7],
           6 : [],
           7 : [] }
assert(cycle_exists(graph4) == False)
print("Graph4 has no cycle.")

#----------------------------------------------------

# If assert raises an error, then a test case was not passed.
print("\nAlgorithm passed all test cases")