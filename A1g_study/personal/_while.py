# # 10952
# while True:
#     a, b = tuple(map(int, input().split()))
    
#     if (a, b) == (0, 0):
#         break

#     print(a + b)

# # 10951
# while True:
#     try:
#         x, y = tuple(map(int, input().split()))
#         print(x + y)
#     except:
#         break

# 1110
init_n = input()

if int(init_n) < 10:
    init_n = '0' + init_n

new_n = init_n[1] + str(int(init_n[0]) + int(init_n[1]))[-1]
count = 1

while int(init_n) != int(new_n):
    new_n = new_n[-1] + str(int(new_n[0]) + int(new_n[-1]))[-1]
    count += 1

print(count)