N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))
DIRECTION = {1: [0, 1], 2: [0, -1], 3: [-1, 0], 4: [1, 0]}
up, bottom, north, south, west, east = 0, 0, 0, 0, 0, 0

for comm in commands:
    m = DIRECTION[comm]
    nx, ny = x + m[0], y + m[1]
    if 0 <= nx < N and 0 <= ny < M:
        if comm == 1:
            bottom, west, up, east = east, bottom, west, up
        elif comm == 2:
            bottom, west, up, east = west, up, east, bottom
        elif comm == 3:
            north, up, south, bottom = up, south, bottom, north
        elif comm == 4:
            north, up, south, bottom = bottom, north, up, south

        if board[nx][ny] == 0:
            board[nx][ny] = bottom
        else:
            bottom = board[nx][ny]
            board[nx][ny] = 0
        x, y = nx, ny
        print(up)

