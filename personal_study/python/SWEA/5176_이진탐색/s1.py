import sys
sys.stdin = open('input.txt')


def in_order(node):
    global k
    if node <= N:
        in_order(node*2)
        k += 1
        tree[node] = k
        in_order(node*2+1)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    k = 0
    in_order(1)
    print(f'#{tc}', tree[1], tree[N//2])

