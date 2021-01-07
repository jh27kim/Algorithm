import sys

'''
N = int(sys.stdin.readline())
dp = [0] * N
dp[0] = 1
dp[1] = 3
for i in range(2, N):
    dp[i] = (dp[i-1] + 2*dp[i-2])%796796
print(dp[-1])
'''


N, M = map(int, sys.stdin.readline().split())
values = [int(sys.stdin.readline()) for _ in range(N)]

dp = [sys.maxsize for _ in range(M+1)]
print(values, dp)

for v in values:
    if v < M:
        dp[v] = 1

for i in range(3, M+1):
    for j in range(1, i-1):
        if dp[j] > 0 and dp[i-j] > 0:
            dp[i] = min(dp[i], dp[j]+dp[i-j])
print(dp[M] if dp[M] < 10000 else -1)

