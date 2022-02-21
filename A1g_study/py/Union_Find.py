import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [0] * (n + 1)

for i in range(1, n+1):
    parent[i] = i

# 유니온 연산 수행
for i in range(m):
    p, a, b = map(int, input().split())
    if p:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')
    else:
        union_parent(parent, a, b)