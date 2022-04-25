# 2869
# import math
# day, night, stick = map(int, input().split())
# result = math.ceil((stick - day) / (day - night)) + 1
# print(result)


# 1929
'''
import math


m, n = map(int, input().split())
array = [True for i in range(n+1)]
array[0] = array[1] = False
for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

for i in range(m, n+1):
    if array[i]:
        print(i)
'''


# 4110

