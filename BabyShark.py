import sys
from collections import deque

N = int(input())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
movement = [[1, 0], [-1, 0], [0, 1], [0, -1]]
queue = deque()
answer = 0


def bfs(queue, size):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    #print(queue)
    i, j = queue[0]
    visited[i][j] = 1
    count = 0

    fish = []
    while queue:
        lenq = len(queue)
        while lenq:
            x, y = queue.popleft()
            for m in movement:
                nx, ny = x + m[0], y + m[1]
                if 0 <= nx < N and 0 <= ny < N:
                    if not visited[nx][ny]:
                        if not board[nx][ny] or board[nx][ny] == size:
                            queue.append([nx, ny])
                            visited[nx][ny] = 1
                        elif board[nx][ny] < size:
                            visited[nx][ny] = 1
                            fish.append([nx, ny, count+1])
            lenq -= 1
        count += 1
        if fish:
            return fish
    return 0


for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            board[i][j] = 0
            queue.append([i, j])

cnt = 0
size = 2
while True:
    cand = bfs(queue, size)
    if not cand:
        print(answer)
        break
    cnt += 1
    cand.sort()
    queue = deque()
    x, y, t = cand[0]
    board[x][y] = 0
    queue.append([x, y])
    answer += t

    if cnt == size:
        size += 1
        cnt = 0

