import sys


sys.stdin = open('input.txt')


def bfs(array, visited):
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for case in highest_pos:
        Q = [case]
        visited[case[0]][case[1]] = 1
        while Q:
            v = Q.pop(0)
            cur_len = visited[v[0]][v[1]] + 1
            for d in dxy:
                ny = v[0] + d[0]
                nx = v[1] + d[1]
                if 0 <= ny < n and 0 <= nx < n:
                    if array[ny][nx] < array[v[0]][v[1]]:
                        visited[ny][nx] = cur_len
                        Q.append((ny, nx))

    return max(list(map(max, visited)))


def climbing(where):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for case in highest_pos:
        Q = [case]
        visited[case[0]][case[1]] = 1
        while Q:
            v = Q.pop(0)
            cur_len = visited[v[0]][v[1]] + 1
            for d in dxy:
                ny = v[0] + d[0]
                nx = v[1] + d[1]
                if 0 <= ny < n and 0 <= nx < n:
                    if array[ny][nx] < array[v[0]][v[1]]:
                        visited[ny][nx] = cur_len
                        Q.append((ny, nx))
                    elif cur_len == where and array[ny][nx] - k < array[v[0]][v[1]]:
                        for i in range(k):
                            new_height = array[ny][nx] - i
                            if new_height < array[v[0]][v[1]]:
                                pass
    return max(list(map(max, visited)))



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

    maxi = climbing(0)
    w = 0
    while w < maxi:
        maxi = max(maxi, climbing(w))
        w += 1

    print(f'#{tc} {maxi}')

