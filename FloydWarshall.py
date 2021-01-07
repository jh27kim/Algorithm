import sys

MAX = sys.maxsize
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
costs = [[0 if i == j else MAX for i in range(N+1)] for j in range(N+1)]

for i in range(M):
    x, y, cost = map(int, sys.stdin.readline().split())
    costs[x][y] = cost

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            continue
        for k in range(1, N+1):
            if i == k or j == k:
                continue
            print(i, j, k)
            costs[i][j] = min(costs[i][j], costs[i][k] + costs[k][j])
print(costs[0:][0:])
