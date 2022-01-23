# 10818
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
"""
n = int(input())
nums = list(map(int, input().split()))

minimum = 1000000
maximum = -1000000

for i in range(0, n):
    if minimum >= nums[i]:
        minimum = nums[i]
    if maximum <= nums[i]:
        maximum = nums[i]
print(minimum, maximum)
"""

# 2562
# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.


"""
num = 0
maximum = 0
nth = 0

for i in range(0, 9):
    num =int(input())
    if maximum <= num:
        maximum = num
        nth = i+1
print(maximum)
print(nth)
"""
# 2577
# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
'''
num = 1
for _ in range(0, 3):
    num *= int(input())

for i in range(0, 10):
    k = 0
    for j in range(0, len(str(num))):
        if str(num)[j] == '{}'.format(i):
            k += 1
    print(k)
'''

# 3052
# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.
'''
nums = list()
rest = list()
for _ in range(0, 10):
    input_num = int(input())
    rest.append(input_num % 42)

for i in range(0, 10):
    if rest[i] not in nums:
        nums.append(rest[i])
print(len(nums))
'''

# 1546
# 세준이는 기말고사를 망쳤다. 세준이는 점수를 조작해서 집에 가져가기로 했다. 일단 세준이는 자기 점수 중에 최댓값을 골랐다. 이 값을 M이라고 한다. 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.
'''
from statistics import mean
n = int(input())
scores = list(map(int, input().split()))
maximum = max(scores)

for i in range(0, n):
    scores[i] = (scores[i] / maximum) * 100

print(mean(scores))
'''

# 8958
# "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다.
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다.
# 예를 들어, 10번 문제의 점수는 3이 된다.
# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
# OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.
'''
n = int(input())
scores = [0] * n
for i in range(0, n):
    result = input()
    current_score = 0
    scores[i] = 0
    for j in range(0, len(result)):
        if result[j] == 'O':
            current_score += 1
            scores[i] += current_score
        else:
            current_score = 0

for i in range(0, n):
    print(scores[i])
'''

# 4344
# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
'''
from statistics import mean
n = int(input())
num_students = list()
for _ in range(0, n):
    scores = list(map(int, input().split()))
    mean_score = mean(scores[1:])
    count = 0
    for i in range(1, len(scores)):
        if scores[i] > mean_score:
            count += 1
    num_students.append(count / scores[0] * 100)

for i in range(0, n):
    print('{:.3f}%'.format(num_students[i]))
'''