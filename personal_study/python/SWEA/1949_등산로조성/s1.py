import sys
sys.stdin = open('input.txt')

'''
1. 일단 재귀형태의 dfs로 탐색
2. 이 때 하나의 경로를 탐색할 때는 갔던 길을 다시 가면 안되지만
    이후에 다른 경로를 탐색하려고 하면 이전 경로에서 지났던 길을 다시 갈 수 있어야함 
3. 따라서 경로를 다 탐색한 뒤에 visited에서 해당 지점을 다시 0으로
4. 중간에 그냥은 갈 수 없지만 공사를 하면 갈 수 있는 지점이 나오면 이 지점부터 bfs로 탐색
5. bfs로 탐색 할 때는 한 번 방문한 지점을 다시 방문해도 됨
    (어차피 하나의 경로 내에서는 높이 문제로 인해 다시 방문할 일이 없기 때문에 다시 방문한다면 새로운 경로)
6. 탐색하는 과정에서 지금까지 가장 길었던 경로보다 더 긴 경로가 발견되면 최대 거리 갱식
'''
from copy import deepcopy


def climbing_before(start, dist, visited):
    global max_len
    visited = deepcopy(visited)
    if max_len < dist:
        max_len = dist
    for d in dxy:
        ny = start[0] + d[0]
        nx = start[1] + d[1]
        if 0 <= ny < n and 0 <= nx < n:
            if array[ny][nx] < array[start[0]][start[1]] and not visited[ny][nx]:
                visited[ny][nx] = dist + 1
                climbing_before((ny, nx), dist+1, visited)
                visited[ny][nx] = 0
            else:
                for i in range(1, k+1):
                    if array[ny][nx] - i < array[start[0]][start[1]] and not visited[ny][nx]:
                        array[ny][nx] -= i
                        climbing_after((ny, nx), dist+1, visited)
                        array[ny][nx] += i


def climbing_after(start, dist, visited):
    global max_len
    visited = deepcopy(visited)
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    Q = [start]
    visited[start[0]][start[1]] = dist
    while Q:
        v = Q.pop(0)
        dist = visited[v[0]][v[1]]
        if dist > max_len:
            max_len = dist
        for d in dxy:
            ny = v[0] + d[0]
            nx = v[1] + d[1]
            if 0 <= ny < n and 0 <= nx < n:
                if array[ny][nx] < array[v[0]][v[1]]:
                    visited[ny][nx] = max(visited[ny][nx], dist + 1)
                    Q.append((ny, nx))


T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    array = []
    highest = 0
    highest_pos = []
    for i in range(n):
        new_line = list(map(int, input().split()))
        array.append(new_line)

        for j in range(n):
            if new_line[j] > highest:
                highest_pos = [(i, j)]
                highest = new_line[j]
            elif new_line[j] == highest:
                highest_pos.append((i, j))
    max_len = 0
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for case in highest_pos:
        visited = [[0 for _ in range(n)] for _ in range(n)]
        visited[case[0]][case[1]] = 1
        climbing_before(case, 1, visited)
    print(f'#{tc} {max_len}')
