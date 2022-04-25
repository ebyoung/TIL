# # 이진탐색 재귀
# def bynary_search_recursion(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     # 값을 찾았을 경우 반환
#     if array[mid] == target:
#         return mid
#     # 값이 중간점 보다 작을 경우 왼쪽 절반 확인
#     elif array[mid] > target:
#         return bynary_search_rec(array, target, start, mid-1)
#     # 값이 중간점 보다 클 경우 오른쪽 절반 확인
#     elif array[mid] < target:
#         return bynary_search_rec(array, target, mid+1, end)


# # 이진탐색 반복
# def binary_search_while(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid - 1
#         elif array[mid] < target:
#             start = mid + 1
#     return None


# 1920
# def is_exist(array, target, start, end):
#     if start > end:
#         return 0
    
#     mid = (start + end) // 2

#     if array[mid] == target:
#         return 1

#     elif array[mid] > target:
#         return is_exist(array, target, start, mid-1)

#     elif array[mid] < target:
#         return is_exist(array, target, mid+1, end)

# n = int(input())
# numbers = list(map(int, input().split()))
# numbers.sort()
# m = int(input())
# targets = list(map(int, input().split()))

# for target in targets:
#     print(is_exist(numbers, target, 0, n-1))


# 10816
from bisect import bisect_left, bisect_right

def count_in_list(cards, number):
    right_index = bisect_right(cards, number)
    left_index = bisect_left(cards, number)
    return right_index - left_index

n = int(input())
cards = list(map(int, input().split()))
cards.sort()
m = int(input())
numbers = list(map(int, input().split()))

results = []
for number in numbers:
    results.append(str(count_in_list(cards, number)))

print(' '.join(results))

# 1654
# k, n = map(int, input().split())
# lengths = []
# for _ in range(k):
#     lengths.append(int(input()))

# start = 0
# end = max(lengths)
# result = 0

# while start <= end:
#     mid = (start + end) // 2
#     count = 0

#     if mid == 0:
#         result = 1
#         break

#     for length in lengths:
#         if length >= mid:
#             count += (length // mid)

#     if count < n:
#         end = mid - 1
    
#     elif count >= n:
#         result = mid
#         start = mid + 1

# print(result)