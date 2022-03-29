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

# 7576
'''
from collections import deque
def bfs(start):
    queue = deque(start)
    while queue:
        v = queue.popleft()
        for d in dxy:
            ny = v[0] + d[0]
            nx = v[1] + d[1]
            if 0 <= ny < N and 0 <= nx < M and not array[ny][nx]:
                array[ny][nx] = array[v[0]][v[1]] + 1
                queue.append((ny, nx))

    result = 0
    for i in range(N):
        for j in range(M):
            if array[i][j]:
                result = max(result, array[i][j])
            else:
                return -1
    return result-1


M, N = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
start = []
for i in range(N):
    for j in range(M):
        if array[i][j] == 1:
            start.append((i, j))
print(bfs(start))
'''

# 2178
'''
from collections import deque


N, M = map(int, input().split())
array = [list(map(int, input())) for _ in range(N)]
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
queue = deque([(0, 0)])

while queue:
    v = queue.popleft()
    if v[0] == N-1 and v[1] == M-1:
        answer = array[v[0]][v[1]]
    for d in dxy:
        ny = v[0] + d[0]
        nx = v[1] + d[1]
        if 0 <= ny < N and 0 <= nx < M and array[ny][nx] == 1:
            queue.append((ny, nx))
            array[ny][nx] = array[v[0]][v[1]] + 1

print(answer)
'''