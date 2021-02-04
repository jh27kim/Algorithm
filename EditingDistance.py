A, B = 'sunday', 'saturday'
sizeA, sizeB = len(A), len(B)

dp = [[0 for _ in range(sizeA+1)] for _ in range(sizeB+1)]
for i in range(1, sizeA+1):
    dp[0][i] = i
for j in range(1, sizeB+1):
    dp[j][0] = j

for i in range(1, sizeB+1):
    for j in range(1, sizeA+1):
        print(i, j)
        dp[i][j] = dp[i-1][j-1] if A[j-1] == B[i-1] else min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])+1

print(dp[-1][-1])
