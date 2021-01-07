from collections import deque


def check(size, x, y, b):
    #print(x, y, size)
    for i in range(size):
        if b[x+i][y+size] != 1 or b[x+size][y+i] != 1:
            return False
    if b[x+size][y+size]:
        return True


def solution(board):
    n, m = len(board), len(board[0])
    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j]:
                size = 1
                if n > i+size and m > j+size:
                    while check(size, i, j, board):
                        size += 1
                        #print(i, j, size, n, m)
                        if n <= i + size or m <= j + size:
                            break
                answer = max(answer, size**2)
    return answer

def solution(board):
    width, height = len(board[0]), len(board)
    for i in range(1, height):
        for j in range(1, width):
            if board[i][j]:
                board[i][j] = min(board[i-1][j-1], min(board[i-1][j], board[i][j-1])) + 1
    return max([item for row in board for item in row])**2


board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
print(solution(board))