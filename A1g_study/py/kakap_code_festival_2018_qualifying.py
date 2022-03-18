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
# B
''''''
import math
import sys
N, K = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
vars = []

for i in range(N-K+1):
    sum_dolls = 0
    for l in range(i, i+K-1):
        sum_dolls += data[l]

    for j in range(i+K-1, N):
        sum_dolls += data[j]
        m = sum_dolls / (j - i + 1)
        var = 0
        for l in range(i, j+1):
            var += (data[l] - m) ** 2
        var /= (j - i + 1)
        vars.append(var)

result = math.sqrt(min(vars))
print(result)
