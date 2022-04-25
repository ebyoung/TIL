# 10172
# print('|\\_/|')
# print('|q p|   /}')
# print('( 0 )"""\\')
# print('|"^"`    |')
# print('||_/=\\\\__|')


# 17471
'''
def check_dfs(sub_set):
    global result
    visited = [0] * (N+1)
    other_set = [x for x in range(1, N+1) if x not in sub_set]
    if sub_set and other_set:
        stack = [sub_set[0]]
        while stack:
            v = stack.pop()
            if not visited[v]:
                visited[v] = 1
                for w in graph[v]:
                    if not visited[w] and w in sub_set:
                        stack.append(w)

        stack = [other_set[0]]
        while stack:
            v = stack.pop()
            if not visited[v]:
                visited[v] = 2
                for w in graph[v]:
                    if not visited[w] and w in other_set:
                        stack.append(w)
        sec1 = 0
        sec2 = 0
        for i in range(1, N+1):
            if visited[i] == 0:
                break
            elif visited[i] == 1:
                sec1 += population[i-1]
            elif visited[i] == 2:
                sec2 += population[i-1]
        else:
            if result == -1:
                result = abs(sec1 - sec2)
            else:
                result = min(result, abs(sec1 - sec2))


N = int(input())
population = list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    data = list(map(int, input().split()))
    graph[i].extend(data[1:])
    for j in range(1, data[0]+1):
        graph[data[j]].append(i)

result = -1

for i in range(1 << N):
    sub_set = []
    for j in range(N):
        if i & (1 << j):
            sub_set.append(j+1)
    check_dfs(sub_set)

print(result)
'''

# 15686
'''
from collections import deque
from copy import deepcopy


def bfs(start, new_array):
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[0] * N for _ in range(N)]
    visited[start[0]][start[1]] = 1
    queue = deque([start])
    while queue:
        v = queue.popleft()
        if new_array[v[0]][v[1]] == 2:
            return visited[v[0]][v[1]] - 1
        for d in dxy:
            ny = v[0] + d[0]
            nx = v[1] + d[1]
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                visited[ny][nx] = visited[v[0]][v[1]] + 1
                queue.append((ny, nx))


def select(idx, ch_list):
    global answer
    if len(ch_list) != M:
        if idx < len(chickens):
            ch_list.append(chickens[idx])
            select(idx+1, ch_list)
            ch_list.pop()
            select(idx+1, ch_list)
        return
    new_array = deepcopy(array)
    for ch_y, ch_x in chickens:
        if (ch_y, ch_x) not in ch_list:
            new_array[ch_y][ch_x] = 0
    total = 0
    for house in houses:
        total += bfs(house, new_array)
        if total > answer:
            break
    else:
        answer = total


N, M = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
houses = []
chickens = []
for i in range(N):
    for j in range(N):
        if array[i][j] == 1:
            houses.append((i, j))
        elif array[i][j] == 2:
            chickens.append((i, j))
answer = N**4
select(0, [])
print(answer)
'''

# 14503
N, M = map(int, input().split())
r, c, d = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
back = [2, 3, 0, 1]
count = 0

while True:
    if not visited[r][c]:
        visited[r][c] = 1
        count += 1
    for _ in range(4):
        if d:
            d -= 1
        else:
            d = 3
        nr = r + dxy[d][0]
        nc = c + dxy[d][1]
        if not array[nr][nc] and not visited[nr][nc]:
            r = nr
            c = nc
            break
    else:
        nr = r + dxy[back[d]][0]
        nc = c + dxy[back[d]][1]
        if array[nr][nc]:
            break
        else:
            r = nr
            c = nc

print(count)
