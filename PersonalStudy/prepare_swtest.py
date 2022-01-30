# 1244 스위치 켜고 끄기
# def change_switch(switches, gender, num):
#     if gender == 1:
#         # 남학생의 경우
#         for i in range(len(switches)//num):
#             # num의 배수 번호에 접근하기 위한 인덱스 생성
#             idx = (i + 1) * num - 1
#             # 해당 인덱스의 요소를 반대로 변경
#             switches[idx] = int(not switches[idx])

#     elif gender == 2:
#         # 여학생의 경우
#         # 최대로 움직일 수 있는 거리 계산
#         max_range = min(num, num_switches-num+1)
#         # 일단 해당 번호의 요소 반대로 변경
#         switches[num-1] = int(not switches[num-1])
#         # 움직일 수 있는 만큼 좌우로 움직이면서
#         for i in range(1, max_range):
#             # 좌우로 같은 거리의 인덱스 생성
#             lidx = num - i - 1
#             ridx = num + i - 1
#             # 좌우로 같은 거리에 있는 요소가 같으면 반대로 변경
#             if switches[lidx] == switches[ridx]:
#                 switches[lidx] = int(not switches[lidx])
#                 switches[ridx] = int(not switches[ridx])
#             # 다르면 반복문 종료
#             else:
#                 break

#     return switches

# # 입력 받기
# num_switches = int(input())
# switches = list(map(int, input().split()))
# num_students = int(input())
# # 성별과 번호 입력을 받아서 정의한 함수를 이용해 처리
# for _ in range(num_students):
#     gender, num = map(int, input().split())
#     switches = change_switch(switches, gender, num)

# # 한줄에 20개씩 출력
# for i in range(num_switches//20 + 1):
#     print(*switches[(i*20):(i+1)*20])


# 2116 주사위 쌓기
# 0-5 1-3 2-4 반대면 찾기 위한 리스트
opposite_side = [5, 3, 4, 1, 2, 0]
# 입력 받기
n = int(input())
dices = []
for _ in range(n):
    dices.append(list(map(int, input().split())))

first_top = {}
for i in range(6):
    if i != dices[0][opposite_side[dices[0].index(6)]]:
        first_top[i] = []

for num in first_top:
    pass


# 2304 창고 다각형
# 2309 일곱 난쟁이
# 2477 참외밭
# 2491 수열
# 2527 색종이
# 2559 경비원
# 2563 빙고 
# 2564 경비원
# 2578 빙고
# 2605 줄 세우기
# 2628 종이자르기
# 2635 수 이어가기
# 2669 직사각형 네개의 합집합의 면적 구하기
# 10157 자리배정
# 10158 개미
# 10163 색종이
# 13300 방 배정
# 14696 딱지놀이