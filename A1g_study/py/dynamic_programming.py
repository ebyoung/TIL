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
# n = int(input())
# array = list(map(int, input().split()))
# array_rev = list(reversed(array))

# dp = []
# inc = [1] * n
# dec = [1] * n
# for i in range(0, n):
#     for j in range(0, i):
#         if array[j] < array[i]:
#             inc[i] = max(inc[i], inc[j] + 1)

#     for j in range(0, i):
#         if array_rev[j] < array_rev[i]:
#             dec[i] = max(dec[i], dec[j] + 1)

# dec.reverse()
# print(inc, dec)
# for i in range(0, n):
#     dp.append(inc[i] + dec[i] - 1)


# print(max(dp))

# # 증가 감소(뒤에서 부터 증가) 나눠서
# n = int(input())
# array = list(map(int, input().split()))
# increase = [1 for _ in range(n)]
# decrease = [1 for _ in range(n)]
# dp = []

# # increse
# for i in range(n):
#     for j in range(i):
#         if array[j] < array[i]:
#             increase[i] = max(increase[i], increase[j] + 1)
# # decrease
# for i in range(n-1, -1, -1):
#     for j in range(n-1, i, -1):
#         if array[i] > array[j]:
#             decrease[i] = max(decrease[i], decrease[j] + 1)

# for i in range(n):
#     dp.append(increase[i] + decrease[i] - 1)

# print(max(dp))


# 9461
# 탑다운
# t = int(input())

# dp = [0] * 101
# dp[0] = dp[1] = dp[2] = dp[3] = 1
# dp[4] = dp[5] = 2

# def padovan(n, dp=dp):
#     if not dp[n]:
#         dp[n] = padovan(n-1) + padovan(n-5)

#     return dp[n]
        
# for _ in range(t):
#     n = int(input())
#     print(padovan(n))

# 바텀업
# t = int(input())
# dp = []
# for i in range(100):
#     if i < 3:
#         dp.append(1)
#     elif i < 5:
#         dp.append(2)
#     else:
#         dp.append(dp[i-1] + dp[i-5])

# for _ in range(t):
#     print(dp[int(input())-1])