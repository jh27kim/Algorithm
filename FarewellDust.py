from collections import deque
import numpy as np
import copy

R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
movement = [[1, 0], [-1, 0], [0, 1], [0, -1]]
n = 0
cleaner = []

for i in range(R):
    if board[i][0] == -1:
        cleaner.append(i)


def dust():
    queue = deque()
    newboard = copy.deepcopy(board)
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                queue.append([i, j])
    while queue:
        x, y = queue.popleft()
        nq = deque()
        cnt = 0
        for m in movement:
            nx, ny = x + m[0], y + m[1]
            if R > nx >= 0 and C > ny >= 0:
                if board[nx][ny] >= 0:
                    cnt += 1
                    nq.append([nx, ny])
        for x1, y1 in nq:
            board[x1][y1] += board[x][y] // 5
            board[x][y] -= board[x][y] // 5
        print(x, y, board[x][y], cnt)
        #board[x][y] = board[x][y] - (cnt * (board[x][y] // 5))
        print(np.asarray(board))

    if clean():
        return 0



def clean():
    global n
    n += 1
    x, y = cleaner
    #print(np.asarray(board))
    for i in range(x-1, 0, -1):
        board[i][0] = board[i-1][0]
    for j in range(y+1, R-1):
        board[j][0] = board[j+1][0]
    for k in range(C-1):
        board[0][k] = board[0][k+1]
        board[-1][k] = board[-1][k+1]
    for l in range(x):
        board[l][C-1] = board[l+1][C-1]
    for m in range(C - 1, y, -1):
        board[m][C-1] = board[m-1][C-1]
    for n in range(C - 1, 1, -1):
        board[x][n] = board[x][n - 1]
        board[y][n] = board[y][n - 1]
    board[x][1], board[y][1] = 0, 0



    if n == T:
        print(sum(item for item in board) + 2)
        return 1
    else:
        return 0

dust()