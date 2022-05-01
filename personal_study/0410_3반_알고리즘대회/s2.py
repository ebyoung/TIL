import sys

sys.stdin = open('input_2.txt')

from copy import deepcopy


def tower(idx, v):
    if idx == k:
        for e in enemy_pos:
            if not v[e[0]][e[1]]:
                break
        else:
            for i in range(k):
                answers[i] = results[i]
        return

    pos = tower_pos[idx]

    for direct_num in range(4):
        fail = False
        visited = deepcopy(v)
        for d in direction[direct_num]:
            ny = pos[0] + d[0]
            nx = pos[1] + d[1]
            while 0 <= ny < n and 0 <= nx < m:
                if array[ny][nx] == '#':
                    break
                if array[ny][nx].isnumeric():
                    fail = True
                    break
                visited[ny][nx] = 1
                ny += d[0]
                nx += d[1]
            if fail:
                break
        else:
            results[idx] = direct_num + 1
            tower(idx+1, visited)
            results[idx] = 0


T = int(input())

for tc in range(1, T + 1):
    n, m, k = map(int, input().split())
    array = [list(input()) for _ in range(n)]
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    direction = [dxy[1::2], dxy[1:3], dxy[::2], dxy[::3]]
    visited = [[0] * m for _ in range(n)]
    results = [0] * k
    answers = [0] * k
    tower_pos = [0] * k
    enemy_pos = []
    for i in range(n):
        for j in range(m):
            if array[i][j].isnumeric():
                tower_pos[int(array[i][j])-1] = (i, j)
            if array[i][j] == '@':
                enemy_pos.append((i, j))
    tower(0, visited)
    for i in range(k):
        if not answers[i]:
            answers[i] = 1
    print(f'#{tc}', *answers)
