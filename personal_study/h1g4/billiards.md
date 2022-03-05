# 당구!



## 각도 거리 계산

```python
import math

start = (1, 1)
end = (2, 2)


a = abs(end[0] - start[0])
b = abs(end[1] - start[1])

r = math.sqrt(a**2 + b**2)
# 이렇게도 가능
r_2 = math.hypot(a, b)
r_3 = math.dist(start, end)

radian = math.atan(b / a)
# degree 변환!!! (중요)
print(r, math.degrees(radian))
```

![ball](billiards.assets/ball.png)

- 거리는 피타고라스 정리, `math.hypot()`, `math.dist()` 중 택
  - `math.hypot()`: 두 변의 길이를 넣으면 피타고라스 정리로 계산해 주는 함수. 근데 직접 계산하는것도 간단해서 큰 차이는 없다.
  - `math.dist()`는 두 점의 좌표를 넣으면 거리를 계산해 주는 함수. 다만 아래같은 예시 상황에서는 사용 어렵다.

- 각도는 아크탄젠트로 계산한 뒤 radian 값을 degree로 변환 필요



```python
# θ를 구하기 위한 코드
whiteBall = (white_x, white_y)
targetBall = (target_x, target_y)
hole = (254, 127)
r = 5.73

#0. 아는 거리 확인
x = 254 - white_x
y = 127 - white_y
a = math.sqrt(x**2 + y**2)
b = math.sqrt(abs(254 - target_x)**2 + abs(127 - target_y)**2)
c = math.sqrt(abs(target_x - white_x)**2 + abs(target_y - white_y)**2)

#1. 흰공, 홀, 목적구가 이루는 각도(C) 계산
C_rad = math.asin((a**2 + b**2 - c**2) / 2*a*b) # 라디안값 반환
```

![image-20220304222926500](billiards.assets/image-20220304222926500.png)