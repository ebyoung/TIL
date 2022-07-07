T = int(input())
oper = [0, lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x // y if y else 1000]
for tc in range(1, T+1):
    N, O, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    operators = list(map(int, input().split()))
    W = int(input())
    visited = [1e3] * 1000
    for number in numbers:
        visited[number] = 1
    queue = numbers[:]
    idx = 0
    # 한 번에 입력 가능한 수
    while idx < len(queue):
        cn = queue[idx]
        for num in numbers:
            nn = int(str(cn) + str(num))
            if 0 <= int(nn) < 1000 and len(str(nn)) < visited[nn]:
                visited[nn] = len(str(nn))
                queue.append(nn)
                numbers.append(nn)
        idx += 1
    if visited[W] != 1000:
        print(f'#{tc}', visited[W])
    else:
        # 연산자를 통해 입력
        while queue:
            cn = queue.pop(0)
            if cn == W:
                break
            for num in numbers:
                for o in operators:
                    nn = oper[o](cn, num)
                    if 0 <= nn < 1000:
                        touch = visited[cn] + visited[num] + 1
                        if touch < visited[nn] and touch < M:
                            visited[nn] = touch
                            queue.append(nn)

        if visited[W] == 1000 or visited[W] >= M:
            visited[W] = -2
        print(f'#{tc}', visited[W]+1)
