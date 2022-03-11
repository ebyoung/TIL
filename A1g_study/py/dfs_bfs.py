# 1260
'''
from collections import deque
n, m, start = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited_d = [0 for _ in range(n+1)]
visited_b = [0 for _ in range(n+1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

stack = [start]
while stack:
    v = stack.pop()
    if not visited_d[v]:
        visited_d[v] = 1
        if graph[v]:
            stack += sorted(graph[v], reverse=True)
        print(v, end=" ")
print()

Q = deque([start])
while Q:
    v = Q.popleft()
    if not visited_b[v]:
        visited_b[v] = 1
        Q += sorted(graph[v])
        print(v, end=" ")
'''

