import sys

sys.stdin = open('input_3.txt')

from collections import deque

def bfs(start, k):
    queue = deque([start])
    dxy = [(1, 0), (-1, 0), (0, 1), (0 ,-1), (1, 1), (-1, -1)]
    visited = [[0] * m for _ in range(n)]
    visited[start[0]][start[1]] = 1
    while queue:
        v = queue.popleft()
        for d in dxy:
            ny = v[0] + d[0]
            nx = v[1] + d[1]
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                visited[ny][nx] = 1
                if array[ny][nx] == k:
                    queue.append((ny, nx))
                else:
                    graph[k].add(array[ny][nx])


def dfs(s, cost, v):
    global min_cost
    if s in end:
        min_cost = min(min_cost, cost)
        return
    visited = v[:]
    for w in graph[s]:
        if w and not visited[w]:
            visited[w] = 1
            dfs(w, cost+nums[w], visited)
            visited[w] = 0


T = int(input())

for tc in range(1, T + 1):
    n, m, k = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(n)]
    nums = [0] * (k + 1)
    start = set()
    end = set()
    graph = [set() for _ in range(k+1)]
    for i in range(n):
        start.add(array[i][0])
        end.add(array[i][m-1])
        for j in range(m):
            if not nums[array[i][j]]:
                bfs((i, j), array[i][j])
            nums[array[i][j]] += 1
    min_cost = n**2
    visited = [0] * (k + 1)
    for s in start:
        if s:
            cost = nums[s]
            visited[s] = 1
            dfs(s, cost, visited)
            visited[s] = 0
    print(f'#{tc}', min_cost)
