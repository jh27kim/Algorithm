N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0
visited = [[0 for _ in range(N)] for _ in range(N)]
diag = [[1, 1], [1, -1], [-1, 1], [1, 1]]


if N == 1:
    if board[0] == 1:
        print(0)
    else:
        print(1)
    exit()


def check(x1, y1, n):
    visited[x1][y1] += n
    for m in diag:
        nx, ny = x1, y1
        while N > nx + m[0] >= 0 and N > ny + m[1] >= 0:
            nx += m[0]
            ny += m[1]
            visited[nx][ny] += n


def dfs(depth, x, y):
    global answer
    #print(x, y)
    answer = max(answer, depth)

    for i in range(x, N):
        y2 = y if i == x else 0
        for j in range(y2, N):
            #print(i, j, depth)
            if board[i][j] and not visited[i][j]:
                check(i, j, 1)
                dfs(depth+1, i, j+1)
                check(i, j, -1)


start = []
for x in range(N):
    for y in range(N):
        if board[x][y]:
            start = [x, y]
            break
    if start:
        break

dfs(0, start[0], start[1])
print(answer)
