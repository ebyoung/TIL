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
# 22016
'''
from collections import deque


def bfs(s):
    visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
    queue = deque([s])
    visited[s[0]][s[1]][0] = 1
    visited[s[0]][s[1]][1] = 1
    while queue:
        v = queue.popleft()
        k = visited[v[0]][v[1]][v[2]]
        if v[0] == N-1 and v[1] == M-1:
            return k
        for d in dxy:
            ny = v[0] + d[0]
            nx = v[1] + d[1]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx][v[2]]:
                if not array[ny][nx]:
                    visited[ny][nx][v[2]] = k + 1
                    queue.append((ny, nx, v[2]))
                elif array[ny][nx] and not v[2]:
                    visited[ny][nx][1] = k + 1
                    queue.append((ny, nx, 1))
    return -1


N, M = map(int, input().split())
array = [list(map(int, input())) for _ in range(N)]
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
answer = bfs((0, 0, 0))
print(answer)
'''

# 7562
'''
from collections import deque

T = int(input())
for _ in range(T):
    l = int(input())
    s = tuple(map(int, input().split()))
    g = tuple(map(int, input().split()))
    dxy = [(i, j) for i in [-2, -1, 1, 2] for j in [-2, -1, 1, 2] if abs(i) != abs(j)]
    visited = [[0] * l for _ in range(l)]
    queue = deque([s])
    while queue:
        v = queue.popleft()
        if v == g:
            print(visited[v[0]][v[1]])
            break

        for d in dxy:
            ny = v[0] + d[0]
            nx = v[1] + d[1]
            if 0 <= ny < l and 0 <= nx < l and not visited[ny][nx]:
                visited[ny][nx] = visited[v[0]][v[1]] + 1
                queue.append((ny, nx))
'''

# 9663
'''
def chess(cy):
    global answer
    if cy == N:
        answer += 1

    for cx in range(N):
        fail = False
        if not row[cx]:
            for d in [(-1, 1), (-1, -1)]:
                ny = cy + d[0]
                nx = cx + d[1]
                while 0 <= ny < N and 0 <= nx < N:
                    if array[ny][nx]:
                        fail = True
                        break
                    ny += d[0]
                    nx += d[1]
                if fail:
                    break
            if not fail:
                array[cy][cx] = 1
                row[cx] = 1
                chess(cy+1)
                array[cy][cx] = 0
                row[cx] = 0


N = int(input())
answer = 0
array = [[0] * N for _ in range(N)]
row = [0] * N
for i in range(N):
    array[0][i] = 1
    row[i] = 1
    chess(1)
    array[0][i] = 0
    row[i] = 0
print(answer)
'''