def dfs_loop1(v):
    stack = [v]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            # print(v, end=' ')
            for w in graph[v]:
                if not visited[w]:
                    stack.append(w)

def dfs_loop2(v):
    stack = [v]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            # print(v, end=' ')
            stack.extend(graph[v])


def dfs_loop3(v):
    stack = [v]
    while stack:
        v = stack.pop()
        visited[v] = 1
        # print(v, end=' ')
        for w in graph[v]:
            if not visited[w] and w not in stack:
                stack.append(w)

import sys

sys.stdin = open('big_graph.txt')
V, E = map(int, input().split())
E = 0
graph = [[]]
for _ in range(V):
    data = list(map(int, input().split()))
    E += len(data)
    graph.append(data)

print('시작')

import time


visited = [0] * (V+1)
start1 = time.time()
dfs_loop1(1)
end1 = time.time()
print(end1 - start1)

visited = [0] * (V+1)
start2 = time.time()
dfs_loop2(1)
end2 = time.time()
print(end2 - start2)

visited = [0] * (V+1)
start3 = time.time()
dfs_loop3(1)
end3 = time.time()
print(end3 - start3)