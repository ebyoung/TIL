# 다익스트라 - [백준 1753](https://www.acmicpc.net/problem/1753)

출발 지점이 정해져있고, 그래프의 모든 지점까지의 거리를 구하는 알고리즘

간선의 비중이 0보다 큰 실수일 때 사용 가능

```python
import heapq

n, m = map(int, input().split())
start = int(input())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    x, y, d = map(int, input().split())
    graph[x][y] = d

INF = float('inf')
dist = [INF] * (n + 1)
# dist[i] : start지점에서 i까지의 거리
dist[start] = 0
heap = [(0, start)]
while heap:
    d, now = heapq.heappop(heap)
    for adj in range(1, n + 1):
        if graph[now][adj]:
            if dist[adj] > dist[now] + graph[now][adj]:
                dist[adj] = dist[now] + graph[now][adj]
                heapq.heappush(heap, (dist[adj], adj))
print(*dist[1:])
```



# 최소 스패닝 트리 - [백준 1197](https://www.acmicpc.net/problem/1197)

예시) 섬들이 여러개 있고, 섬들간의 거리를 구할 수 있다

다리를 지어 섬들을 모두 이을 때, 다리 길이의 합이 최소가 되게 하는 거 구하기.

```python
from sys import stdin as s
from sys import setrecursionlimit as stlim

stlim(10 ** 6)

v, e = map(int, s.readline().split())

connection = []
for _ in range(e):
    connection.append(list(map(int, s.readline().split())))
connection.sort(key=lambda n: n[-1])

parent = list(range(v + 1))


def find(target):
    if target == parent[target]:
        return target
    parent[target] = find(parent[target])
    return parent[target]


def union(a, b):
    x = find(a)
    y = find(b)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
    return


i = 1
ans = 0
for line in connection:
    if find(line[0]) != find(line[1]):
        union(line[0], line[1])
        i += 1
        ans += line[2]
    if i == v:
        break
print(ans)
```



# DP

점화식 세우는 문제

