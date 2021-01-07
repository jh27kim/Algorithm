from collections import deque


def bfs(x, y):
    q.append([x, y])
    visited[x][y] = 1
    while q:
        lenq = len(q)
        while lenq:
            x, y = q.popleft()
            for m in movement:
                nx, ny = x + m[0], y + m[1]
                if h > nx >= 0 and w > ny >= 0:
                    if not visited[nx][ny] and board[nx][ny] == ".":
                        visited[nx][ny] = visited[x][y] + 1
                        q.append([nx, ny])
                elif nx < 0 or ny < 0 or nx >= h or ny >= w:
                    print(visited[x][y])
                    return
            lenq -= 1
        fire()
    print('IMPOSSIBLE')
    return


def fire():
    flen = len(fqueue)
    while flen:
        x, y = fqueue.popleft()
        for m in movement:
            nx, ny = x + m[0], y + m[1]
            if h > nx >= 0 and w > ny >= 0:
                if board[nx][ny] == ".":
                    fqueue.append([nx, ny])
                    board[nx][ny] = "*"
        flen -= 1


T = int(input())
for _ in range(T):
    w, h = map(int, input().split())
    board = [list(input()) for _ in range(h)]

    q, fqueue = deque(), deque()
    movement = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    visited = [[0 for _ in range(w)] for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if board[i][j] == "*":
                fqueue.append([i, j])
            if board[i][j] == "@":
                sx, sy = i, j
                board[i][j] = "."

    fire()
    bfs(sx, sy)
