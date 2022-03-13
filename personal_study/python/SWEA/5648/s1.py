import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    n = int(input())
    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))



    print(f'#{tc} ')

