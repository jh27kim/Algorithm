import sys
from collections import deque

N, M = map(int, input().split())
score_map = [[] for _ in range(N+1) for _ in range(N+1)]
visit = [[0 if i == j else 10000 for j in range(N+1)] for i in range(N+1)]
queue = deque([1])
answer = 0

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    visit[A][B] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            visit[i][j] = min(visit[i][j], visit[i][k] + visit[k][j])


for x in range(1, N+1):
    count = 0
    for y in range(1, N+1):
        if visit[x][y] != 10000 or visit[y][x] != 10000:
            count += 1
    if count == N:
        answer += 1
print(answer)
