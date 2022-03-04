# 당구!



## 각도 거리 계산

```python
import math

start = (1, 1)
end = (2, 2)


a = abs(end[0] - start[0])
b = abs(end[1] - start[1])

r = math.sqrt(a**2 + b**2)

radian = math.atan(b / a)
# degree 변환!!! (중요)
print(r, math.degrees(radian))
```

![ball](billiards.assets/ball.png)

- 거리는 피타고라스 정리
- 각도는 아크탄젠트로 계산한 뒤 radian 값을 degree로 변환 필요



```python
# θ를 구하기 위한 코드
```

![image-20220304222926500](billiards.assets/image-20220304222926500.png)