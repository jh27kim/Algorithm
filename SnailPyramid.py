def solution(n):
    board = [[0 for _ in range(i)] for i in range(1, n + 1)]
    y, x = -1, 0
    number = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                y += 1
            elif i % 3 == 1:
                x += 1
            elif i % 3 == 2:
                y -= 1
                x -= 1
            board[y][x] = number
            number += 1
    from itertools import chain
    return [i for i in chain(*board)]

n = 4
print(solution(n))