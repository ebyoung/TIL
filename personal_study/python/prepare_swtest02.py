# 2578 빙고
# 부르는 숫자를 x로 만들고 매번 빙고가 몇개인지 확인했다.
# zip함수를 쓰면 튜플 형태로 묶이는걸 생각 안하고 리스트와 비교하는 실수를 했다.
'''
def check_bingo(data):
    data_t = list(map(list, zip(*data)))
    bingo = ['x', 'x', 'x', 'x', 'x']
    diag1 = []
    diag2 = []
    count = 0

    for i in range(5):
        if data[i] == bingo:
            count += 1
        if data_t[i] == bingo:
            count += 1
        diag1.append(data[i][i])
        diag2.append(data[4-i][i])

    if diag1 == bingo:
        count += 1
    if diag2 == bingo:
        count += 1
    if count > 2:
        return True
    return False


data = [list(map(int, input().split())) for _ in range(5)]
call_num = [-1]
bingo_count = 0
for _ in range(5):
    call_num.extend(list(map(int, input().split())))

for i in range(1, 26):
    for j in range(5):
        if call_num[i] in data[j]:
            data[j][data[j].index(call_num[i])] = 'x'
            break

    if check_bingo(data):
        result = i
        break

print(result)
'''

# 2605 줄 세우기
# insert와 음수 인덱스를 활용해 뒤에서부터 뽑은 번호 번째 자리에 넣어준다.
# 0을 뽑는 경우엔 마지막 자리에 넣어줘야 하는데 잘못 처리해서 틀렸다.
'''
n = int(input())
array = []
data = list(map(int, input().split()))
for i in range(n):
    if data[i]:
        idx = -1 * data[i]
    else:
        idx = len(array)
    array.insert(idx, i+1)
print(*array)
'''

# 2628 종이자르기
# 자르는 위치를 통해 새로 생기는 가로 세로 길이를 모아 넓이를 구한다.
#
'''
w, h = map(int, input().split())
n = int(input())
cut = {0: [0], 1: [0]}
w_h = [[], []]
result = 0

for _ in range(n):
    d, l = map(int, input().split())
    cut[d].append(l)

cut[0].append(h)
cut[1].append(w)

for i in range(2):
    cut[i].sort()
    for j in range(1, len(cut[i])):
        w_h[i].append(cut[i][j] - cut[i][j-1])

for y in w_h[0]:
    for x in w_h[1]:
        result = max(result, x * y)

print(result)
'''


# 2635 수 이어가기
# 시키는대로 수를 이어가면서 가장 긴 경우를 저장해둔다.
# 양의 정수와 음의 정수는 0을 포함하지 않는데 이 부분을 신경써주지 않았다.
# 반복문의 범위를 n까지가 아니라 n+1까지 해줘야 n이 1일때도 반복문이 돌아간다.
'''
n = int(input())
max_len = 2
result = [n, 1]

for i in range(1, n+1):
    array = [n, i]
    next_num = n - i
    while next_num >= 0:
        array.append(next_num)
        next_num = array[-2] - array[-1]

    if len(array) > max_len:
        result = array
        max_len = len(array)

print(max_len)
print(*result)
'''

# 2669 직사각형 네개의 합집합의 면적 구하기
# 100*100 2차원 배열을 만들어서 색칠한다.
# 갈수록 생각을 안하고 문제가 시키는 그대로 하는 거 같은데 이래도 되는지 모르겠다.
'''
array = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            array[i][j] = 1

print(sum(map(sum, array)))
'''

# 10157 자리배정
# 달팽이..?
# 달팽이 때 처럼 한칸씩 이동 할 필요 없이 주어진 값이 나오지 않으면 dk만큼 이동해 한 변을 통채로 넘어갔다.
'''
c, r = map(int, input().split())
n = int(input())
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
if n > c * r:
    print(0)
else:
    k = r
    xy = [1, r]
    i = 1
    d = 0
    while k < n:
        d = (d + 1) % 4
        dk = c - i
        if k + dk >= n:
            break
        xy[0] += dk * dxy[d][0]
        xy[1] += dk * dxy[d][1]
        k += dk
        d = (d + 1) % 4
        dk = r - i
        if k + dk >= n:
            break
        xy[0] += dk * dxy[d][0]
        xy[1] += dk * dxy[d][1]
        k += dk
        i += 1

    xy[0] += (n - k) * dxy[d][0]
    xy[1] += (n - k) * dxy[d][1]

    print(*xy)
'''

# 10158 개미
#
# 일단 벽까지 계속 가다가 다음 벽까지 갈 수 없으면 남은 시간 만큼만 이동하는 식으로 풀어봤는데 제한시간 초과가 나왔다.
'''
dxy = [1, 1]
w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

while True:
    if dxy[0] == 1:
        dp = w - p
    else:
        dp = p

    if dxy[1] == 1:
        dq = h - q
    else:
        dq = q

    dpq = min(dp, dq)

    if t < dpq:
        break

    p += dxy[0] * dpq
    q += dxy[1] * dpq
    t -= dpq

    if dp <= dq:
        dxy[0] *= -1

    if dp >= dq:
        dxy[1] *= -1

p += dxy[0] * t
q += dxy[1] * t
print(p, q)
'''

# 10163 색종이
#
#

n = int(input())
array = [[0 for _ in range(1001)] for _ in range(1001)]
for k in range(1, n+1):
    x, y, w, h = map(int, input().split())
    for i in range(h):
        for j in range(w):
            array[y+i][x+j] = k

for k in range(1, n+1):
    total = 0
    for i in range(1001):
        total += array[i].count(k)
    print(total)




# 13300 방 배정
# 14696 딱지놀이
