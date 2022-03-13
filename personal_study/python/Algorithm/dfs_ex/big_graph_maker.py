# 짱큰그래프
inp = []
V = 15000
import random
for i in range(V):
    for _ in range((V-i)//2):
        j = random.randint(i, V)
        inp.append(i)
        inp.append(j)
    print(i)

E = len(inp)//2
graph = [set() for _ in range(V+1)]
for i in range(E):
    graph[inp[i*2]].add(inp[i*2+1])
    graph[inp[i*2+1]].add(inp[i*2])

f = open("./big_graph.txt", 'w')
f.write(f'{V} {E}\n')
for line in graph:
    line = map(str, list(line))
    f.write(' '.join(line)+'\n')
f.close()