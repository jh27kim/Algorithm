import numpy as np

board = [[0 for _ in range(20)] for _ in range(20)]


def check(x, y, l, n, m):
    if x + 1 - l < 0 or y + l > n:
        return False

    for i in range(l+1):
        for j in range(l+1):
            if board[x-i][y+j]:
                return False
    return True


def place(x, y, length, n, m):
    for i in range(x, -1, -1):
        for j in range(y, n):
            if check(i, j, length, n, m):
                for a in range(i-1, i-length, -1):
                    for b in range(j+1, j+length):
                        board[a][b] = 1

                return i, j, True
        y = 0

    return 0, 0, False


def solution(n, m, rectangle):
    answer = []
    x, y = m-1, 0
    rectangle.sort(key=lambda x:x[0])

    for length, num in rectangle:
        for i in range(num):
            nx, ny, possible = place(x, y, length, n, m)
            if not possible:
                return answer
            answer.append([ny, m-1-nx, length])
            if ny + length < m:
                ny += length
            else:
                if nx > 0:
                    nx -= 1
                    ny = 0
                else:
                    return answer
            x, y = nx, ny

    return answer


n = 7
m = 8
rectangle = [[2,2],[1,4],[3,2]]
print(solution(n, m, rectangle))