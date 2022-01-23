# # 1330
# nums = list(map(int, input().split()))

# if nums[0] > nums[1]:
#     print('>')
# elif nums[0] < nums[1]:
#     print('<')
# else:
#     print('==')


# # 9498
# score = int(input())

# if score >= 90:
#     print('A')
# elif score >= 80:
#     print('B')
# elif score >= 70:
#     print('C')
# elif score >= 60:
#     print('D')
# else:
#     print('F')

# # 2753
# year = int(input())
# if year % 4 == 0:
#     if year % 100 != 0:
#         print(1)
#     else:
#         if year % 400 == 0:
#             print(1)
#         else:
#             print(0)
# else:
#     print(0)

# # 14681
# x = int(input())
# y = int(input())

# if x > 0:
#     if y > 0:
#         print(1)
#     else:
#         print(4)
# else:
#     if y > 0:
#         print(2)
#     else:
#         print(3)

# 2884
# h, m = tuple(map(int, input().split()))

# if m >= 45:
#     m -= 45
#     print(h, m)
# else:
#     if h == 0:
#         h = 23
#         m += 15
#         print(h, m)
#     else:
#         h -= 1
#         m += 15
#         print(h, m)