# 1717
'''
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
'''

# 1976
'''
def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    p[find_set(y)] = find_set(x)


N = int(input())
M = int(input())
p = [x for x in range(N)]
data = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if data[i][j]:
            union(i, j)
city = list(map(int, input().split()))
plan = set()
for x in city:
    plan.add(find_set(x-1))
if len(plan) == 1:
    print('YES')
else:
    print('NO')
'''

# 4195
'''
def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    px = find(x)
    py = find((y))
    if px != py:
        parents[py] = px
        num_friends[px] += num_friends[py]


T = int(input())
for _ in range(T):
    F = int(input())
    parents = {}
    num_friends = {}
    for _ in range(F):
        friends = input().split()
        for f in friends:
            if not parents.get(f):
                parents[f] = f
                num_friends[f] = 1
        union(*friends)
        print(num_friends[find(friends[0])])
'''