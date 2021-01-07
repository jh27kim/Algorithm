import sys
from collections import deque
import copy

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
movement = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visited = [[0 for _ in range(M)] for _ in range(N)]
queue = deque()
answer = 0
walls = []


def bfs(walls):
    global queue, board
    q = copy.deepcopy(queue)
    b = copy.deepcopy(board)
    area = 0

    for x1, y1 in walls:
        b[x1][y1] = 1


    while q:
        x, y = q.popleft()
        for m in movement:
            nx, ny = x + m[0], y + m[1]
            if 0 <= nx < N and 0 <= ny < M:
                if b[nx][ny] == 0:
                    q.append([nx, ny])
                    b[nx][ny] = 2

    for x in range(N):
        for y in range(M):
            if b[x][y] == 0:
                area += 1

    return area


def dfs(walls, a, b):
    global answer
    if len(walls) == 3:
        answer = max(answer, bfs(walls))
        return

    for x in range(a, N):
        if x != a:
            b = 0
        for y in range(b, M):
            if board[x][y] == 0:
                walls.append([x, y])
                dfs(walls, x, y+1)
                walls.pop()


for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            queue.append([i, j])

dfs(walls, 0, 0)
print(answer)

import random
print(random.randint(1, 48))