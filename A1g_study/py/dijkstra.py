# 18352
''''''
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
