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

