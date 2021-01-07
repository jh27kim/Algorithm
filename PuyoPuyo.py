from collections import deque

board = [list(input()) for _ in range(12)]
colors = ['R', 'G', 'B', 'P', 'Y']
movement = [[1, 0], [-1, 0], [0, 1], [0, -1]]
queue = deque()


def sorting():
    for column in range(6):
        dots, ndots = [], []
        for row in range(11, -1, -1):
            if board[row][column] != ".":
                ndots.append(board[row][column])
        while len(ndots) != 12:
            ndots.append(".")
        for r in range(11, -1, -1):
            board[r][column] = ndots[11-r]


def bfs(col):
    nq = deque()
    nq.append(queue[-1])
    visited = [[0 for _ in range(6)] for _ in range(12)]
    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1
        for m in movement:
            nx, ny = x + m[0], y + m[1]
            if 12 > nx >= 0 and 6 > ny >= 0:
                if board[nx][ny] == col and not visited[nx][ny]:
                    queue.append([nx, ny])
                    visited[nx][ny] = 1
                    nq.append([nx, ny])

    if len(nq) >= 4:
        for x1, y1 in nq:
            board[x1][y1] = "."
        return True

    else:
        return False

cnt = 0
while True:
    ind = []
    for c in colors:
        for i in range(12):
            for j in range(6):
                if board[i][j] == c:
                    queue.append([i, j])
                    ind.append(bfs(c))
    if not any(ind):
        break
    else:
        cnt += 1
    sorting()
print(cnt)
