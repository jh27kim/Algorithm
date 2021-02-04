n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for i in range(j)] for j in range(1, n+1)]
dp[0][0] = triangle[0][0]

for i in range(1, len(triangle)):
    for j in range(len(triangle[i])):
        if j == 0:
            triangle[i][j] += triangle[i-1][j]
        elif j == len(triangle[i]) - 1:
            triangle[i][j] += triangle[i-1][j-1]
        else:
            triangle[i][j] = max(triangle[i-1][j] + triangle[i][j], triangle[i-1][j-1] + triangle[i][j])

print(max(triangle[-1]))