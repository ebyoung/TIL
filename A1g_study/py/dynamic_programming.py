# 1003
# top_down
# import sys
# n = int(sys.stdin.readline())

# dp = [[1, 0], [0, 1]]

# def fib_01(num):
#     if num < len(dp):
#         return dp[num]
#     else:
#         result = [fib_01(num-2)[0] + fib_01(num-1)[0], fib_01(num-2)[1] + fib_01(num-1)[1]]
#         dp.append(result)
#         return result
    
# for _ in range(n):
#     print(*fib_01(int(sys.stdin.readline())))

# bottom_up
# import sys
# n = int(sys.stdin.readline())

# dp = [[1, 0], [0, 1]]

# def fib_01(num):
#     if num >= len(dp):
#         for i in range(len(dp), num+1):
#             next_01 = [dp[i-2][0] + dp[i-1][0], dp[i-2][1]+ dp[i-1][1]]
#             dp.append(next_01)

#     return dp[num]

# for _ in range(n):
#     print(*fib_01(int(sys.stdin.readline())))


# 9184
# import sys

# w_dict = {}
# def w(a, b, c):
#     if w_dict.get((a, b, c)):
#         return w_dict.get((a, b, c))

#     if (a <= 0) or (b <= 0) or (c <= 0):
#         w_dict[(a, b, c)] = 1
#         return 1

#     elif (a > 20) or (b > 20) or (c > 20):
#         result = w(20, 20, 20)
#         w_dict[(a, b, c)] = result
#         return result

#     elif (a < b) and (b < c):
#         result = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
#         w_dict[(a, b, c)] = result
#         return result
    
#     else:
#         result = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
#         w_dict[(a, b, c)] = result
#         return result

# while True:
#     a, b, c = map(int, sys.stdin.readline().split())
#     if (a == -1) and (b == -1) and (c == -1):
#         break
#     print(f'w({a}, {b}, {c}) = {w(a, b, c)}')


# 11053
# n = int(input())
# array = list(map(int, input().split()))

# def lis(array, d):
#     for i in range(1, len(array)):
#         for j in range(0, i):
#             if array[j] < array[i]:
#                 d[i] = max(d[i], d[j] + 1)
#     return max(d)

# d = [1] * n
# print(lis(array, d))


# 11054
n = int(input())
array = list(map(int, input().split()))

dp = []
inc = [1] * n
dec = [1] * n
for i in range(0, n):
    for j in range(0, i):
        if array[j] < array[i]:
            inc[i] = max(inc[i], inc[j] + 1)
    for j in range(i, n):
        if array[j] < array[i]:
            dec[i] = max(dec[i], dec[j] + 1)

print(inc, dec)


print(dp)