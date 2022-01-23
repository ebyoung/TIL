# 2739
# num = int(input())
# for i in range(1, 10):
#     print(f'{num} * {i} = {num*i}')

# 10950
# t = int(input())
# for _ in range(t):
#     num1, num2 = map(int, input().split())
#     print(num1 + num2)

# 8393
# num = int(input())
# total = 0

# while num:
#     total += num
#     num -= 1

# print(total)

# 15552
# import sys

# t = int(sys.stdin.readline())

# for _ in range(t):
#     num1, num2 = map(int, sys.stdin.readline().split())
#     print(num1 + num2)

# 2741
# num = int(input())
# for i in range(1, num+1):
#     print(i)

# 11021
# t = int(input())
# for i in range(t):
#     num1, num2 = map(int, input().split())
#     print(f'Case #{i+1}: {num1+num2}')

# 11022
# t = int(input())
# for i in range(t):
#     num1, num2 = map(int, input().split())
#     print(f'Case #{i+1}: {num1} + {num2} = {num1+num2}')

# 2438
# num = int(input())
# for i in range(num):
#     print('*' * (i+1))

# 2439
# num = int(input())
# for i in range(1, num+1):
#     print(' ' * (num - i) + '*' * i)

# 10871
# n, x = map(int, input().split())
# numbers = list(map(int, input().split()))

# 반복문 돌기 76ms
# for number in numbers:
#     if x > number:
#         print(number, end = ' ')

# 리스트 만들기 76ms
# smaller_than_x = [number for number in numbers if x > number]
# print(*smaller_than_x)