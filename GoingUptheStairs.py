import sys

N = int(sys.stdin.readline())
stairs = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
dp = [stairs[0]]
if N == 1 or N == 2:
    print(sum(stairs))
    exit()
dp.append(max(dp[0]+stairs[1], stairs[1]))
dp.append(max(dp[0]+stairs[2], stairs[1] + stairs[2]))

for i in range(3, N):
    dp.append(max(stairs[i] + stairs[i-1] + dp[i-3], stairs[i] + dp[i-2]))
print(dp[-1])
