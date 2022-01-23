# 1316
n = int(input())
result = 0
for _ in range(n):
    word = input()
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            if word[i] in word[i+1:]:
                break
    else:
        result += 1

print(result)