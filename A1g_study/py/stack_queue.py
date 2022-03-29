# 수업시간 예제
# n = int(input())

# 처음 입력 받기 외우기
# nums = list(map(int, input().split()))
# words = list(input().split())

# # 1

# for idx in range(1, n+1):
#     words = list(input().split())
#     stack = []
#     for word in words:
#         stack.append(word)
#     result = []
#     for _ in range(len(stack)):
#         word = stack.pop()
#         result.append(word)
#     a = ' '.join(result)
#     print('Case #{}:{}'.format(idx, a))

# 팰린드롬인지 확인하기
# word = input()
# chars = []
# result = []
# for i in range(len(word)):
#     chars.append(word[i])
#     stack = []
# for char in chars:
#     stack.append(char) 
# for _ in range(len(stack)):
#     palindrome = stack.pop()
#     result.append(palindrome)
# if chars == result:
#     print(1)
# else:
#     print(0)

# 카드1
# from collections import deque
# num = int(input())

# queue = deque()

# for i in range(1, num+1):
#     queue.append(i)
# print(queue.popleft())    
# for _ in range(len(queue)):
#     queue.insert(len(queue)+1, queue.popleft())
#     print(queue.popleft())