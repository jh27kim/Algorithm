N = int(input())
M = int(input())
ing = list(map(int, input().split()))
answer = 0
low = []
high = []
ing.sort()

for i in ing:
    if i < M/2:
        low.append(i)
    else:
        high.append(i)

for i in low:
    for j in high:
        if i + j >= M:
            if i + j == M:
                answer += 1
            break

print(answer)
