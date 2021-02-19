import sys

N, K = map(int, input().split())
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
stuff = [[0, 0]]

for _ in range(N):
    stuff.append(list(map(int, input().split())))

for i in range(1, N+1):
    w, v = stuff[i]
    for j in range(1, K+1):
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

print(dp[N][K])
