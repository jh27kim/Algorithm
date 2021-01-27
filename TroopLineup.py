import sys

N = int(input())
troops = list(map(int, sys.stdin.readline().split()))
answer = [1] * N

for i in range(1, N):
    for j in range(i):
        if troops[j] > troops[i]:
            answer[i] = max(answer[i], answer[j] + 1)

print(N-max(answer))
