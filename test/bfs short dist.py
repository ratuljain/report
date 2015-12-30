__author__ = 'rjain1'
import collections

g = {
    'A': ['B', 'C'],
    'B': ['C'],
    'C': ['A', 'D', 'E'],
    'D': ['A'],
    'E': ['D', 'G'],
    'F': ['H'],
    'G': ['E', 'F'],
    'H': ['G']
}


# def bfs(graph, root):
#     for node in graph:
        

print bfs(g, 'C', 'H')

# t = input('')
# for i in range(t):
#     l,n = [int(x) for x in raw_input('').split(',')]
#     ladders = {int(y.split(',')[0]):int(y.split(',')[1]) for y in raw_input('').split(' ')}
#     snakes = {int(y.split(',')[0]):int(y.split(',')[1]) for y in raw_input('').split(' ')}
#     board = [100] * 100
#     board[0] = 0
#     for i in range(100):
#         j = i + 1
#         for j in range(j, j+6):
#             if j >= 100:
#                 break
#             board[j] = min(board[j], board[i] + 1)
#         if i in ladders:
#             board[ladders[i]] = min(board[ladders[i]], board[i])
#         if i in snakes:
#             if board[i] < board[snakes[i]]:
#                 board[snakes[i]] = board[i]
#                 i = snakes[i]
#
#     print board[99]
