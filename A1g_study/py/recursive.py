# 10872
# def factorial(n):
#     if n <= 1:
#         return 1
    
#     return n * factorial(n-1)

# n = int(input())
# print(factorial(n))


# 10870
# def fib(n):
#     if n <= 1:
#         return n
    
#     return fib(n-1) + fib(n-2)

# n = int(input())
# print(fib(n))


# 2447 다시
# def print_star(n, stars):
#     out = []

#     if n == 3:
#         return stars

#     for star_block in stars:
#         out.append(star_block * 3)

#     for star_block in stars:
#         out.append(star_block + ' ' * len(stars) + star_block)

#     for star_block in stars:
#         out.append(star_block * 3)
        
#     return print_star(n/3, out)


# n = int(input())
# first = ['***', '* *', '***']
# for print_line in print_star(n, first):
#     print(print_line)



# 11729 
# import sys
# sys.setrecursionlimit(1000000)

# def hanoi(n, start, end):
#     sticks = [1, 2, 3]
#     sticks.remove(start)
#     sticks.remove(end)
#     spare = sticks.pop()  # 대신에 6 - start - end 하면 남는 수 알 수 있음

#     if n == 1:
#         print(start, end)   # 요기서 print
#         return  # 그리고 리턴만 적어서 함수를 끝내줘야함
    
#     hanoi(n-1, start, spare)
#     print(start, end)   # 이친구도 그냥 print
#     hanoi(n-1, spare, end)

# n = int(input())
# print((2**n)-1) # 수학적으로 계산 가능, 굳이 따로 만들필요 없음
# hanoi(n, 1, 3)


# 5568
# 1.
# from itertools import permutations
#
# n = int(input())
# k = int(input())
# data = [input() for _ in range(n)]
# count = 0
# nums = list(permutations(data, k))
# num_set = set()
# for num in nums:
#     num_set.add(int(''.join(num)))
# print(len(num_set))

# 2.
# def make_nums(cards, data):
#     global num_set
#     if len(cards) == k:
#         num_set.add(int(''.join(cards)))
#     else:
#         for i in range(len(data)):
#             num = data.pop(i)
#             make_nums(cards + [num], data)
#             data.insert(i, num)
#
#
# n = int(input())
# k = int(input())
# data = [input() for _ in range(n)]
# count = 0
# num_set = set()
# make_nums([], data)
# print(len(num_set))
