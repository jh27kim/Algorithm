import copy

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
stack = []
answer = -int(1e9)
movement = [[-1, 0], [0, -1], [1, 0], [0, 1]]


def move(stack):
    global answer
    new_board = copy.deepcopy(board)

    for direction in stack:
        if direction == 0:
            for j in range(N):
                ind = 0
                for i in range(1, N):
                    if new_board[i][j]:
                        temp = new_board[i][j]
                        new_board[i][j] = 0
                        if new_board[ind][j] == 0:
                            new_board[ind][j] = temp
                        elif new_board[ind][j] == temp:
                            new_board[ind][j] *= 2
                            ind += 1
                        else:
                            ind += 1
                            new_board[ind][j] = temp

        elif direction == 1:
            for i in range(N):
                ind = 0
                for j in range(1, N):
                    if new_board[i][j]:
                        temp = new_board[i][j]
                        new_board[i][j] = 0
                        if new_board[i][ind] == 0:
                            new_board[i][ind] = temp
                        elif new_board[i][ind] == temp:
                            new_board[i][ind] *= 2
                            ind += 1
                        else:
                            ind += 1
                            new_board[i][ind] = temp

        elif direction == 2:
            for j in range(N):
                ind = N-1
                for i in range(N-2, -1, -1):
                    if new_board[i][j]:
                        temp = new_board[i][j]
                        new_board[i][j] = 0
                        if new_board[ind][j] == 0:
                            new_board[ind][j] = temp
                        elif new_board[ind][j] == temp:
                            new_board[ind][j] *= 2
                            ind -= 1
                        else:
                            ind -= 1
                            new_board[ind][j] = temp

        else:
            for i in range(N):
                ind = N-1
                for j in range(N-2, -1, -1):
                    if new_board[i][j]:
                        temp = new_board[i][j]
                        new_board[i][j] = 0
                        if new_board[i][ind] == 0:
                            new_board[i][ind] = temp
                        elif new_board[i][ind] == temp:
                            new_board[i][ind] *= 2
                            ind -= 1
                        else:
                            ind -= 1
                            new_board[i][ind] = temp




        '''m = movement[direction]
        if direction >= 2:
            start = N-1
            end = -1
            step = -1
        else:
            start = 0
            end = N
            step = 1

        for x in range(start, end, step):
            for y in range(start, end, step):
                nx, ny = x + m[0], y + m[1]
                while 0 <= nx < N and 0 <= ny < N:
                    if new_board[nx][ny] == new_board[x][y]:
                        new_board[x][y] = 0
                        new_board[nx][ny] *= 2
                        break
                    elif new_board[nx][ny] != new_board[x][y]:
                        if new_board[nx][ny] == 0:
                            new_board[nx][ny] = new_board[x][y]
                            new_board[x][y] = 0
                            x, y = nx, ny
                            nx += m[0]
                            ny += m[1]
                            continue

                        nx -= m[0]
                        ny -= m[1]
                        if not(nx == x and ny == y):
                            new_board[nx][ny] = new_board[x][y]
                            new_board[x][y] = 0
                        break
                    nx += m[0]
                    ny += m[1]'''


    local_max = -1
    for i in range(N):
        for j in range(N):
            local_max = max(local_max, new_board[i][j])

    answer = max(answer, local_max)


def dfs(stack):
    if len(stack) == 5:
        move(stack)
        return

    for i in range(4):
        stack.append(i)
        dfs(stack)
        stack.pop()

dfs(stack)
print(answer)
