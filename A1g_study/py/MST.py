# 4386
'''
import math


def find_set(x):
    if parents[x] != x:
        parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    parents[find_set(y)] = parents[x]


def kruskal():
    global answer
    edge_cnt = idx = 0
    while edge_cnt < n-1:
        x, y = edges[idx][:2]
        if find_set(x) != find_set(y):
            union(x, y)
            edge_cnt += 1
            answer += edges[idx][2]
        idx += 1


n = int(input())
xys = [list(map(float, input().split())) for _ in range(n)]
edges = []
for i in range(n):
    for j in range(i+1, n):
        edges.append((i, j, round(math.dist(xys[i], xys[j]), 3)))
edges.sort(key = lambda x: x[2])
answer = 0
parents = [x for x in range(n)]
kruskal()
print(answer)
'''

# 1922
'''
def find_set(x):
    if parents[x] != x:
        parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    parents[find_set(y)] = parents[x]


def kruskal():
    answer = 0
    edge_count = idx = 0
    while edge_count < N - 1:
        x, y = edges[idx][:2]
        if find_set(x) != find_set(y):
            union(x, y)
            edge_count += 1
            answer += edges[idx][2]
        idx += 1
    return answer


N = int(input())
M = int(input())
edges = [tuple(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x: x[2])
parents = list(range(N+1))
print(kruskal())
'''