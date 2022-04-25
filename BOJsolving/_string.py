# 1316
# n = int(input())
# result = 0
# for _ in range(n):
#     word = input()
#     for i in range(len(word)-1):
#         if word[i] != word[i+1]:
#             if word[i] in word[i+1:]:
#                 break
#     else:
#         result += 1

# print(result)


# 11654
# char = input()
# print(ord(char))


# 11720
# n = int(input())
# num_str = input()
# print(sum(map(int, [*num_str])))


# 10809
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# s = input()
# result = []
# for char in alphabet:
#     result.append(s.find(char))

# print(*result)


# 12904
# s = input()
# t = input()
#
# while len(t) > len(s):
#     if t[-1] == 'A':
#         t = t[:-1]
#     elif t[-1] == 'B':
#         t = t[:-1]
#         t = t[::-1]
#
# print(int(bool(t == s)))
