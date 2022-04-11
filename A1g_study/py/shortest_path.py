# 1753
'''
import sys


INF = int(1e9)
n, m = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
'''

# 18352
'''
import heapq


N = int(input())
M = int(input())
graph = [[1e9] * (N + 1) for _ in range(N+1)]
dist = [1e9] * (N + 1)
visited = [0] * (N + 1)
for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s][e] = min(graph[s][e], w)
A, B = map(int, input().split())

heap = []
heapq.heappush(heap, (0, A))
while heap:
    w, v = heapq.heappop(heap)
    if not visited[v]:
        visited[v] = 1
        dist[v] = w
        for i in range(1, N+1):
            if not visited[i]:
                heapq.heappush(heap, (dist[v] + graph[v][i], i))
print(dist[B])
'''

# 17472
'''
다시풀기
from collections import deque


def bfs(s, num):
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque([s])
    array[s[0]][s[1]] = num
    while queue:
        v = queue.popleft()
        for d in dxy:
            ny = v[0] + d[0]
            nx = v[1] + d[1]
            if 0 <= ny < N and 0 <= nx < M and array[ny][nx] == 1:
                array[ny][nx] = num
                queue.append((ny, nx))


N, M = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
num = 2
for i in range(N):
    for j in range(M):
        if array[i][j] == 1:
            bfs((i, j), num)
            num += 1
'''

# 1238
'''
import heapq

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
graph_inv = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))
    graph_inv[e].append((s, t))

heap = []
dist_go = [int(1e6)] * (N + 1)
visited = [0] * (N + 1)
heapq.heappush(heap, (0, X))
while heap:
    w, v = heapq.heappop(heap)
    if not visited[v]:
        dist_go[v] = w
        visited[v] = 1
        for x, t in graph[v]:
            if not visited[x]:
                heapq.heappush(heap, (min(dist_go[x], dist_go[v] + t), x))

heap = []
dist_back = [int(1e6)] * (N + 1)
visited = [0] * (N + 1)
heapq.heappush(heap, (0, X))
while heap:
    w, v = heapq.heappop(heap)
    if not visited[v]:
        dist_back[v] = w
        visited[v] = 1
        for x, t in graph_inv[v]:
            if not visited[x]:
                heapq.heappush(heap, (min(dist_back[x], dist_back[v] + t), x))

print(max(list(map(sum, zip(dist_go, dist_back)))[1:]))
'''

# 1261
'''
import heapq

M, N = map(int, input().split())
array = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
heap = [(0, 0, 0)]

while heap:
    w, cy, cx = heapq.heappop(heap)
    if (cy, cx) == (N - 1, M - 1):
        break

    for d in dxy:
        ny = cy + d[0]
        nx = cx + d[1]
        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
            visited[ny][nx] = visited[cy][cx] + array[ny][nx]
            heapq.heappush(heap, (visited[ny][nx], ny, nx))

print(visited[N-1][M-1]-1)
'''