# 1244 스위치 켜고 끄기
'''
def change_switch(switches, gender, num):
    if gender == 1:
        # 남학생의 경우
        for i in range(len(switches)//num):
            # num의 배수 번호에 접근하기 위한 인덱스 생성
            idx = (i + 1) * num - 1
            # 해당 인덱스의 요소를 반대로 변경
            switches[idx] = int(not switches[idx])

    elif gender == 2:
        # 여학생의 경우
        # 최대로 움직일 수 있는 거리 계산
        max_range = min(num, num_switches-num+1)
        # 일단 해당 번호의 요소 반대로 변경
        switches[num-1] = int(not switches[num-1])
        # 움직일 수 있는 만큼 좌우로 움직이면서
        for i in range(1, max_range):
            # 좌우로 같은 거리의 인덱스 생성
            lidx = num - i - 1
            ridx = num + i - 1
            # 좌우로 같은 거리에 있는 요소가 같으면 반대로 변경
            if switches[lidx] == switches[ridx]:
                switches[lidx] = int(not switches[lidx])
                switches[ridx] = int(not switches[ridx])
            # 다르면 반복문 종료
            else:
                break

    return switches

# # 입력 받기
# num_switches = int(input())
# switches = list(map(int, input().split()))
# num_students = int(input())
# # 성별과 번호 입력을 받아서 정의한 함수를 이용해 처리
# for _ in range(num_students):
#     gender, num = map(int, input().split())
#     switches = change_switch(switches, gender, num)

# 한줄에 20개씩 출력
for i in range(num_switches//20 + 1):
    print(*switches[(i*20):(i+1)*20])
'''

# 2116 주사위 쌓기
'''
# 0-5 1-3 2-4 반대면 찾기 위한 리스트
opposite_side = [5, 3, 4, 1, 2, 0]
# 입력 받기
n = int(input())
dices = []
for _ in range(n):
    dices.append(list(map(int, input().split())))

# 합의 최소값을 저장하기 위한 변수
max_sum = 0
# 첫 윗면을 1부터 6까지 한번씩 확인
for num in range(1, 7):
    top_num = num
    current_sum = 0
    # 주사위를 하나씩 쌓아가며
    for dice in dices:
        # 1부터 6까지 담긴 리스트를 만들고
        one_to_six = [i for i in range(1, 7)]
        # 이전 주사위의 윗면이자 현재 주사위의 바닥면을 빼고
        one_to_six.remove(top_num)
        bottom_idx = dice.index(top_num)
        # 현재 주사위의 윗면 숫자를 구하고
        top_num = dice[opposite_side[bottom_idx]]
        # 현재 주시위의 윗면 숫자도 빼고
        one_to_six.remove(top_num)
        # 남은 수중 가장 큰 수를 합계에 더해줌
        current_sum += max(one_to_six)
    # 이번 합과 지금까지 가장 컸던 합을 비교해 더 큰값 저장
    max_sum = max(current_sum, max_sum)

print(max_sum)
'''

# 2304 창고 다각형
'''
# 입력 받기
n = int(input())
columns = []
for _ in range(n):
    l, h = map(int, input().split())
    columns.append((l, h))

# 일단 위치를 기준으로 정렬
columns.sort(key=lambda x:x[0])
# 리스트 분할
l_list = [columns[i][0] for i in range(n)]
h_list = [columns[i][1] for i in range(n)]

# 가장 높이가 높은 기둥의 인덱스 확인
max_idx = h_list.index(max(h_list))
# 일단 첫번째 기둥 높이 저장
current_max = h_list[0]
# 넓이를 저장할 변수
total = 0
# 가장 높은 기둥이 나오기 전에는
for i in range(1, max_idx+1):
    # 지금까지 가장 높았던 기둥의 높이를 넓이에 계속 더해줌
    total += current_max * (l_list[i] - l_list[i-1])
    current_max = max(current_max, h_list[i])
# 가장 높은 기둥의 차례가 오면 높이를 한번만 더해줌
total += h_list[max_idx]
# 마지막 기둥이 나올 때 까지
while max_idx != (n-1):
    # 남은 기둥 중 가장 높은 기둥을 확인해
    next_max_idx = h_list.index(max(h_list[max_idx+1:]), max_idx+1)
    # 해당 기둥이 나올때 까지 그 기둥의 높이만큼을 넓이에 더해줌
    total += (l_list[next_max_idx] - l_list[max_idx]) * h_list[next_max_idx]
    max_idx = next_max_idx

print(total)
'''

# 2309 일곱 난쟁이
'''
from itertools import permutations
# 입력 받기
heights = []
for _ in range(9):
    heights.append(int(input()))


for case in permutations(heights, 7):
    if sum(case) == 100:
        case = sorted(list(case))
        break

for height in case:
    print(height)

# permutations 사용x
heights = []
for _ in range(9):
    heights.append(int(input()))

def find_dwarfs(heights):
    for i in range(9):
        for j in range(i+1, 9):
            false_dwarfs = [heights[i], heights[j]]
            if (sum(heights) - sum(false_dwarfs)) == 100:
                result = sorted([height for height in heights if height not in false_dwarfs])
                return result

for height in find_dwarfs(heights):
    print(height)
'''

# 2477 참외밭
'''
입력 받아서 리스트로 저장
k = int(input())
lengths = []
for i in range(6):
    direction, length = map(int, input().split())
    lengths.append(length)

# 1. 방향 정보를 어떻게 활용해야 하는지 모르겠다ㅠ
# 2. 가장 긴 변을 위쪽에 두면 결국 모양은 둘 중 하나
#       가장 긴 변            가장 긴 변
#     _____________         ______________
#  -1 |_______    | +1   -1 |    ________| +1
#      -2  -3 |___|         |___| +3  +2

max_idx = lengths.index(max(lengths))
left = lengths[max_idx-1]
right = lengths[(max_idx+1) % 6]
if left > right: # 왼쪽과 오른쪽 중 더 긴 변을 확인
    big_square = lengths[max_idx] * lengths[max_idx - 1]
    small_square = lengths[(max_idx + 2) % 6] * lengths[(max_idx + 3) % 6]
    print(k * (big_square - small_square))
else:
    big_square = lengths[max_idx] * lengths[(max_idx + 1) % 6]
    small_square = lengths[(max_idx - 2)] * lengths[(max_idx - 3)]
    print(k * (big_square - small_square))
'''

# 2491 수열
'''
n = int(input())                            # 입력 받기
array = list(map(int, input().split()))
increasing = [1] * n                        # 연속해서 커지는 수열을 기록하기 위한 리스트
decreasing = [1] * n                        # 연속해서 작아지는 수열을 기록하기 위한 리스트
for i in range(1, n):
    if array[i] >= array[i-1]:              # 이전 값보다 크거나 같으면
        increasing[i] = increasing[i-1] + 1 # 증가 수열 리스트에 기록
    if array[i] <= array[i-1]:              # 이전 값보다 작거나 같으면
        decreasing[i] = decreasing[i-1] + 1 # 감소 수열 리스트에 기록

print(max(max(decreasing), max(increasing)))
'''

# 2527 직사각형
def check(s1, s2):
    array = [[0] * 50001 for _ in range(50001)]

for _ in range(4):
    data = list(map(int, input().split()))
    print(check(data[:4], data[4:]))





# 2559 수열
# 2563 색종이
# 2564 경비원