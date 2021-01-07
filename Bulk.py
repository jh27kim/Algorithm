N = int(input())
spec = []
answer = []

for i in range(N):
    spec.append(list(map(int, input().split())))

for j in range(N):
    rank = 1
    for k in range(N):
        if k == j:
            continue
        if spec[k][0] > spec[j][0] and spec[k][1] > spec[j][1]:
            rank += 1
    print(rank, end=" ")
