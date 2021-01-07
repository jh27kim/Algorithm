N, M = map(int, input().split())
x, y, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def change(d):
    if(d == 0):
        return 3
    elif(d == 1):
        return 0
    elif(d == 2):
        return 1
    elif(d == 3):
        return 2

cnt = 1
board[x][y] = 2
while True:
    dc = d
    for i in range(4):
        moved = False
        dc = change(dc)
        nx, ny = x + dx[dc], y + dy[dc]
        if N > nx >= 0 and M > ny >= 0 and board[nx][ny] == 0:
            cnt += 1
            x, y = nx, ny
            board[nx][ny] = 2
            d = dc
            moved = True
            break

    if not moved:
        if (d == 0):
            x += 1
        elif (d == 1):
            y -= 1
        elif (d == 2):
            x -= 1
        elif (d == 3):
            y += 1

        if board[x][y] == 1:
            break

print(cnt)
