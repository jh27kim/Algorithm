from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
queue = deque()
movement = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visited = [[0 for _ in range(m)] for _ in range(n)]


def bfs(q):
    w = 1
    while q:
        x, y = q.popleft()
        for mv in movement:
            nx, ny = x + mv[0], y + mv[1]
            if n > nx >= 0 and m > ny >= 0:
                if board[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                    w += 1
    return w


area, cnt = 0, 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            visited[i][j] = 1
            queue.append([i, j])
            area = max(area, bfs(queue))


print(cnt)
print(area)
