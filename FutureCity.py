import sys

MAX = sys.maxsize
N, M = map(int, sys.stdin.readline().split())
costs = [[0 if i == j else MAX for j in range(N+1)] for i in range(N+1)]

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    costs[x][y] = 1
    costs[y][x] = 1

X, K = map(int, sys.stdin.readline().split())

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j: continue
        for k in range(1, N+1):
            if i == k or j == k: continue
            costs[i][j] = min(costs[i][j], costs[i][k] + costs[k][j])
print(costs)
print(costs[1][K] + costs[K][X])
