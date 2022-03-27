import sys
sys.stdin = open('input.txt')


def heap_push(num):
    global heap_size
    heap_size += 1
    tree[heap_size] = num
    child = heap_size
    parent = heap_size//2
    while tree[child] < tree[parent]:
        tree[child], tree[parent] = tree[parent], tree[child]
        child = parent
        parent = child//2


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    heap_size = 0
    tree = [0] * (len(data)+1)
    for num in data:
        heap_push(num)
    result = 0
    while heap_size:
        heap_size //= 2
        result += tree[heap_size]

    print(f'#{tc}', result)

