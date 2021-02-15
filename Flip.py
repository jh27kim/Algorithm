N, M = map(int, input().split())
board = []

for _ in range(N):
    row = input()
    board.append(list(row))

'''
dp = [[0 for _ in range(M)] for _ in range(N)]
dp[0][0] = 2

for i in range(1, M):
    if board[0][i] == board[0][i-1]:
        dp[0][i] = dp[0][i-1] * 2
    else:
        if dp[0][i-1] == 1:
            dp[0][i] = 1
        else:
            dp[0][i] = dp[0][i-1] // 2

for j in range(1, N):
    if board[j][0] == board[j-1][0]:
        dp[j][0] = dp[j-1][0] * 2
    else:
        if dp[j-1][0] == 1:
            dp[j][0] = 1
        else:
            dp[j][0] = dp[j-1][0] // 2

for i in range(1, N):
    for j in range(1, M):
        if board[i][j] == board[i-1][j] == board[i][j-1] == board[i-1][j-1]:
            dp[i][j] = dp[i-1][j] * dp[i][j-1]
        elif board[i-1][j] != board[i][j-1]:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1])
        else:
            if board[i][j] == board[i-1][j]:
                dp[i][j] = dp[i-1][j] * 2
            else:
                if dp[i][j-1] == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j-1]//2

#print(dp)
print(dp[-1][-1])

'''
visited = [[0 for _ in range(M)] for _ in range(N)]
movement = [[1, 0], [-1, 0], [0, 1], [0, -1]]
count = 0

for i in range(N):
    for j in range(M):
        for m in movement:
            nx, ny = i + m[0], j + m[1]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] != board[i][j]:
                    count += 1
                    break

print(pow(2, M*N-count)%(int(1e9)+7))