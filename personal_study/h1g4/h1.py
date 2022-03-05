import math

start = (1, 1)
end = (2, 2)


a = abs(end[0] - start[0])
b = abs(end[1] - start[1])

r = math.sqrt(a**2 + b**2)
r_2 = math.hypot(a, b)
r_3 = math.dist(start, end)

radian = math.atan(b / a)
# degree 변환!!! (중요)
print(r, r_2, r_3, math.degrees(radian))


# 당구각 예시
ro4 = lambda x: round(x, 4)

white_x = 244
white_y = ro4(127 - math.sqrt(3) * 10)
target_x = 254
target_y = 117

# θ를 구하기 위한 코드
whiteBall = (white_x, white_y)
targetBall = (target_x, target_y)
hole = (254, 127)
r = 5.73

#0. 아는 거리 확인
x = 254 - white_x
y = 127 - white_y
# a = math.sqrt(x**2 + y**2)
# b = math.sqrt(abs(254 - target_x)**2 + abs(127 - target_y)**2)
# c = math.sqrt(abs(target_x - white_x)**2 + abs(target_y - white_y)**2)
a = math.dist(whiteBall, hole)
b = math.dist(targetBall, hole)
c = math.dist(whiteBall, targetBall)

#1. 흰 공, 홀, 목적구가 이루는 각도(C) 계산
cos_C = (a**2 + b**2 - c**2) / (2*a*b)
C = math.acos(cos_C) # 라디안값


#2. d(흰 공이 충돌까지 이동할 거리) 계산
# d = math.sqrt((a * math.sin(C))**2 + ((b+2*r) - a*cos_C)**2)
d = math.hypot((a * math.sin(C)), ((b + 2*r) - a*cos_C))

#3. 홀, 흰 공, 흰 공의 이동경로가 이루는 각도 ang2 계산
cos_ang2 = (a**2 + d**2 - (b+2*r)**2) / (2*a*d)
ang2 = math.acos(cos_ang2)

#4. 나머지 각도 ang1 계산
ang1 = math.atan(x / y)

#5. 실제 구하고자 하는 각도는 ang1 + ang2
angle1 = ro4(math.degrees(ang1 + ang2))
print(angle1, math.degrees(ang2))