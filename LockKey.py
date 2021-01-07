def check(key, lock, x, y):
    M, N = len(key), len(lock)
    board = [[0 for _ in range(N+(2*M)-2)] for _ in range(N+(2*M)-2)]

    for i in range(x, x+M):
        for j in range(y, y+M):
            board[i][j] += key[i-x][j-y]

    for i in range(M-1, N+M-1):
        for j in range(M-1, N+M-1):
            board[i][j] += lock[i-M+1][j-M+1]
            if board[i][j] != 1:
                return False
    return True


def move(key, lock):
    M, N = len(key), len(lock)

    for i in range(N+M-1):
        for j in range(N+M-1):
            if check(key, lock, i, j):
                return True
    return False


def rotate(key):
    M = len(key)
    temp = [[0 for _ in range(M)] for _ in range(M)]
    for i in range(M):
        for j in range(M):
            temp[i][j] = key[M-j-1][i]
    return temp


def solution(key, lock):
    for i in range(4):
        if move(key, lock):
            return True
        key = rotate(key)
    return False



key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))