import sys
sys.stdin = open('input_1.txt')


T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    coins = sorted(list(map(int, input().split())))
    n_coins = 0
    while m > 0:
        coin = coins.pop()
        n_coins += m // coin
        m %= coin
    print(f'#{tc}', n_coins)

