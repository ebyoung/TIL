# 1806
'''
n, s = map(int, input().split())
data = list(map(int, input().split()))

min_len = n + 1
interval_sum = 0
end = 0
for start in range(n):
    while end < n:
        if interval_sum + data[end] >= s:
            min_len = min(min_len, end - start + 1)
            break
        interval_sum += data[end]
        end += 1

    interval_sum -= data[start]

if min_len == n + 1:
    min_len = 0
print(min_len)
'''

