# 11047
# n, target = map(int, input().split())

# coins = list()

# for _ in range(n):
#     coins.append(int(input()))

# result = 0
# while target:
#     coin = coins.pop()
    
#     if target < coin:
#         continue
    
#     result += target // coin
#     target %= coin

# print(result)

# 1931
# n = int(input())
# data = list()

# for _ in range(n):
#     start, end = map(int, input().split())
#     data.append((start, end))

# data.sort(key=lambda x: x[0])
# data.sort(key=lambda x: x[1])

# count = 1
# end = data[0][-1]

# for i in range(1, n):
#     if end <= data[i][0]:
#         count += 1
#         end = data[i][-1]

# print(count)

# 왜 아니지ㅠ
# for _ in range(n):
#     start, end = map(int, input().split())
#     data.append((start, end, end-start))

# data.sort(key=lambda x: x[2])

# schedule = [data[0]]
# for i in data:
#     for j in schedule:
#         if not (((i[0] < j[0]) and (i[1] <= j[0])) or ((i[0] >= j[1]) and (i[1] > j[1]))):
#             break
#     else:
#         schedule.append(i)

# print(len(schedule), schedule)

# 11399
# n = int(input())
# data = list(map(int, input().split()))

# data.sort()
# result = 0

# for i in range(n):
#     result += sum(data[:i+1])

# print(result)

# 1541
# expressions = input()
# # -되는 수를 최대한 크게 만들기
# # 일단 -를 기준으로 분리 -> +를 먼저 계하고 나중에 - 계산하기 위해
# step1 = expressions.split('-')
# # 첫 - 앞부분은 어쩔 수 없이 + 진행
# result = sum(list(map(int, step1[0].split('+'))))
# # 이후로는 +를 먼저 계산해 최대한 큰 수를 만들고 한번에 - 계산
# for step2 in step1[1:]:
#     result -= sum(list(map(int, step2.split('+'))))

# print(result)

# 13305
# n = int(input())
# distances = list(map(int, input().split()))
# prices = list(map(int, input().split()))
# min_price = prices[0]
# result = distances[0] * min_price

# for i in range(1, n-1):

#     if min_price < prices[i]:
#         result += min_price * distances[i]
#     else:
#         min_price = prices[i]
#         result += min_price * distances[i]

# print(result)