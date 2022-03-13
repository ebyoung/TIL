# 14502 연구소1
'''
from itertools import combinations
from copy import deepcopy

def safty_area(lab):
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    stack = []
    stack.extend(xys[2])
    while stack:
        v = stack.pop()
        for d in dxy:
            ny = v[0] + d[0]
            nx = v[1] + d[1]
            if 0 <= ny < n and 0 <= nx < m and not lab[ny][nx]:
                lab[ny][nx] = 2
                stack.append((ny, nx))

    count = 0
    for i in range(n):
        for j in range(m):
            if not lab[i][j]:
                count += 1

    return count

n, m = map(int, input().split())
laboratory = []

for _ in range(n):
    laboratory.append(list(map(int, input().split())))

xys = [[], [], []]

for i in range(n):
    for j in range(m):
        xys[laboratory[i][j]].append((i, j))

cases = list(combinations(xys[0], 3))
result = 0
for case in cases:
    lab_case = deepcopy(laboratory)
    for i, j in case:
        lab_case[i][j] = 1

    count = safty_area(lab_case)
    if result < count:
        result = count

print(result)
'''

# 17141 연구소2
'''
from itertools import combinations
from collections import deque
from copy import deepcopy

def spread_virus(lab):
    Q = deque(case)
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while Q:
        v = Q.popleft()
        for d in dxy:
            ny = v[0] + d[0]
            nx = v[1] + d[1]
            if 0 <= ny < n and 0 <= nx < n and not lab[ny][nx]:
                Q.append((ny, nx))
                lab[ny][nx] = lab[v[0]][v[1]] + 1

    maxi = 0

    for i in range(n):
        for j in range(n):
            k = lab[i][j]
            if k:
                maxi = max(maxi, k)
            else:
                return n**2

    return maxi - 2


n, m = map(int, input().split())
laboratory = []

for _ in range(n):
    laboratory.append(list(map(int, input().split())))

xys = [[], [], []]

for i in range(n):
    for j in range(n):
        xys[laboratory[i][j]].append((i, j))

cases = list(combinations(xys[2], m))

result = n**2

for case in cases:
    lab_case = deepcopy(laboratory)

    for xy2 in xys[2]:
        if xy2 not in case:
            lab_case[xy2[0]][xy2[1]] = 0

    result = min(result, spread_virus(lab_case))

if result == n**2:
    print(-1)
else:
    print(result)
'''

# 17142 연구소3
''''''

