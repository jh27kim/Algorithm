import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
S, X, Y = map(int, sys.stdin.readline().split())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
time = 0
temp = []

for i in range(N):
    for j in range(N):
        if board[i][j]:
            temp.append((board[i][j], i, j))

temp.sort()
queue = deque(temp)

while S:
    lenq = len(queue)
    while lenq:
        virus, x, y = queue.popleft()
        for m in range(4):
            nx, ny = x + dx[m], y + dy[m]
            if 0 <= nx < N and 0 <= ny < N:
                if not board[nx][ny]:
                    board[nx][ny] = virus
                    queue.append((virus, nx, ny))
        lenq -= 1
    S -= 1
print(board[X-1][Y-1])
