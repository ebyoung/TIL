# 10172
# print('|\\_/|')
# print('|q p|   /}')
# print('( 0 )"""\\')
# print('|"^"`    |')
# print('||_/=\\\\__|')


# 17471
'''
def check_dfs(sub_set):
    global result
    visited = [0] * (N+1)
    other_set = [x for x in range(1, N+1) if x not in sub_set]
    if sub_set and other_set:
        stack = [sub_set[0]]
        while stack:
            v = stack.pop()
            if not visited[v]:
                visited[v] = 1
                for w in graph[v]:
                    if not visited[w] and w in sub_set:
                        stack.append(w)

        stack = [other_set[0]]
        while stack:
            v = stack.pop()
            if not visited[v]:
                visited[v] = 2
                for w in graph[v]:
                    if not visited[w] and w in other_set:
                        stack.append(w)
        sec1 = 0
        sec2 = 0
        for i in range(1, N+1):
            if visited[i] == 0:
                break
            elif visited[i] == 1:
                sec1 += population[i-1]
            elif visited[i] == 2:
                sec2 += population[i-1]
        else:
            if result == -1:
                result = abs(sec1 - sec2)
            else:
                result = min(result, abs(sec1 - sec2))


N = int(input())
population = list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    data = list(map(int, input().split()))
    graph[i].extend(data[1:])
    for j in range(1, data[0]+1):
        graph[data[j]].append(i)

result = -1

for i in range(1 << N):
    sub_set = []
    for j in range(N):
        if i & (1 << j):
            sub_set.append(j+1)
    check_dfs(sub_set)

print(result)
'''

# 17779

