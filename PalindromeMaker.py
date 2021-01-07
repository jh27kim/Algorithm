N = int(input())
p = list(map(int, input().split()))
dp = [[-1 for _ in range(N)] for _ in range(N)]


def pelin(x, y):
    print(dp)
    if dp[x][y] != -1:
        return dp[x][y]
    if x >= y:
        dp[x][y] = 0
        return dp[x][y]
    if p[x] == p[y]:
        dp[x][y] = pelin(x+1, y-1)
    else:
        dp[x][y] = min(pelin(x, y-1), pelin(x+1, y)) + 1
    return dp[x][y]


for i in range(N):
    for j in range(N):
        pelin(i, j)
print(dp[0][N-1])
