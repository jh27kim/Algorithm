import copy

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
smell = [[0 for _ in range(N)] for _ in range(N)]

directions = list(map(int, input().split()))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
priority = []
answer = 0
print(directions)
for _ in range(M):
    temp = []
    for _ in range(4):
        temp.append(list(map(int, input().split())))
    priority.append(temp)


for x in range(N):
    for y in range(N):
        if board[x][y]:
            smell[x][y] = (board[x][y], K)


def shark_move(board):
    global smell
    new_board = copy.deepcopy(board)
    smell_updates = []
    for x in range(N):
        for y in range(N):
            if board[x][y]:
                found = False
                shark_number = board[x][y]
                nd = directions[shark_number-1] - 1

                movement_priority = priority[shark_number-1][nd]

                for m in movement_priority:
                    nx, ny = x + dx[m-1], y + dy[m-1]
                    if 0 <= nx < N and 0 <= ny < N and not smell[nx][ny]:
                        if new_board[nx][ny] == 0 or shark_number < new_board[nx][ny]:
                            new_board[nx][ny] = shark_number
                            smell_updates.append([nx, ny, shark_number])
                        directions[shark_number - 1] = m
                        new_board[x][y] = 0
                        found = True
                        break
                if found:
                    continue

                for m in movement_priority:
                    nx, ny = x + dx[m - 1], y + dy[m - 1]
                    if 0 <= nx < N and 0 <= ny < N:
                        if smell[nx][ny]:
                            if smell[nx][ny][0] == shark_number:
                                if new_board[nx][ny] == 0 or shark_number < new_board[nx][ny]:
                                    new_board[nx][ny] = shark_number
                                    smell_updates.append([nx, ny, shark_number])
                                directions[shark_number - 1] = m
                                new_board[x][y] = 0
                                break

    smell = smell_map(smell_updates)
    return new_board


def smell_map(smell_updates):
    global smell
    for i in range(N):
        for j in range(N):
            if smell[i][j] != 0:
                shark_number, smell_count = smell[i][j]
                smell_count -= 1
                if smell_count == 0:
                    smell[i][j] = 0
                else:
                    smell[i][j] = (shark_number, smell_count)

    for x, y, num in smell_updates:
        if smell[x][y] != 0:
            if smell[x][y][0] > num:
                smell[x][y] = (num, K)
        else:
            smell[x][y] = (num, K)

    return smell


def check():
    cnt = 0
    for x in range(N):
        for y in range(N):
            if board[x][y]:
                cnt += 1
    return True if cnt == 1 else False


while True:
    board = shark_move(board)
    answer += 1
    if check():
        print(answer)
        break

    if answer >= 1000:
        print(-1)
