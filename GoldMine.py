import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    mine = list(map(int, sys.stdin.readline().split()))
    dp = [[0]*M for _ in range(N)]
    for i in range(0, len(mine), M):
        dp[i//M][0] = mine[i]

    for y in range(1, M):
        for x in range(N):
            if x == 0:
                dp[x][y] = max(dp[x][y-1], dp[x+1][y-1]) + mine[x*M + y]
            elif x == N-1:
                dp[x][y] = max(dp[x][y - 1], dp[x-1][y-1]) + mine[x*M + y]
            else:
                dp[x][y] = max(dp[x][y - 1], dp[x + 1][y - 1], dp[x-1][y-1]) + mine[x * M + y]

    answer = 0
    for i in range(N):
        answer = max(answer, dp[i][-1])
    print(answer)

