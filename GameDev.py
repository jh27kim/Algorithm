import sys

N, M = map(int, sys.stdin.readline().split())
A, B, d = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
movement = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}
visited = [[0 for _ in range(M)] for _ in range(N)]
x, y = A, B
visited[x][y] = 1
answer = 1

while True:
    moved = False
    temp_d = (d+2) % 4
    for i in range(4):
        d = (d + 3) % 4
        nx, ny = x + movement[d][0], y + movement[d][1]
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and not board[nx][ny]:
                x, y = nx, ny
                visited[x][y] = 1
                moved = True
                answer += 1
                break

    if not moved:
        nx, ny = x + movement[temp_d][0], y + movement[temp_d][1]
        if board[nx][ny]:
            break
        else:
            x, y = nx, ny

print(answer)
