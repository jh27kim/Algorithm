import sys
from collections import deque
import numpy as np

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, input())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
movement = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visited[0][0] = 1
queue = deque()
queue.append([0, 0])
answer = 1

while queue:
    lenq = len(queue)
    while lenq:
        x, y = queue.popleft()
        for m in movement:
            nx, ny = x + m[0], y + m[1]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and board[nx][ny]:
                    queue.append([nx, ny])
                    board[nx][ny] = board[x][y] + 1
                    visited[nx][ny] = 1
        lenq -= 1
    answer += 1
    if visited[N-1][M-1]:
        break
    print(np.asarray(visited), answer)
print(answer)
