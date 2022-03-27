import sys
sys.stdin = open('input.txt')


def subtree(node):
    global count

    if node:
        count += 1
        subtree(tree[node][0])
        subtree(tree[node][1])

T = int(input())

for tc in range(1, T+1):
    E, N = map(int ,input().split())
    data = list(map(int, input().split()))
    tree = [[0, 0, 0] for _ in range(E+2)]
    for i in range(E):
        if tree[data[i*2]][0]:
            tree[data[i*2]][1] = data[i*2+1]
        else:
            tree[data[i*2]][0] = data[i*2+1]
        tree[data[i*2+1]][2] = data[i*2]
    count = 0
    subtree(N)

    print(f'#{tc}', count)

