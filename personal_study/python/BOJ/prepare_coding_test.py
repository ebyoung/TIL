# 1753 다익스트라
import sys
import heapq
V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

INF = float('INF')
dist = [INF] * (V + 1)
dist[K] = 0
heap = [(0, K)]
while heap:
    d, v = heapq.heappop(heap)
    if dist[v] < d:
        continue

    for w in graph[v]:
        if dist[w[0]] > d + w[1]:
            dist[w[0]] = d + w[1]
            heapq.heappush(heap, (dist[w[0]], w[0]))

for i in range(1, V+1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])