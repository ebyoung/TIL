# A
'''
def money(a, b):
    result = 0
    reward2017 = [500, 300, 200, 50, 30, 10]
    k = 0
    if a:
        for i in range(1, 7):
            k += i
            if a <= k:
                result += reward2017[i-1]
                break
    k = 0
    if b:
        for i in range(5):
            k += 2**i
            if b <= k:
                result += 2**(9-i)
                break

    return result*10000


T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(money(a, b))
'''