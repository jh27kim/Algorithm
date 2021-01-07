from collections import deque

M, N = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
visited = [[0 for _ in range(M)] for _ in range(N)]
movement = [[1, 0], [-1, 0], [0, -1], [0, 1]]


def bfs(q):
    w = 0
    nq = deque()
    while q:
        x, y = q.popleft()
        for m in movement:
            nx, ny = x + m[0], y + m[1]
            if N > nx >= 0 and M > ny >= 0:
                if visited[nx][ny] == 0 and tomatoes[nx][ny] == 0:
                    visited[nx][ny] = 1
                    nq.append([nx, ny])
        if not q:
            w += 1
            q = nq
            nq = deque()
    return w


for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            queue.append([i, j])
        if tomatoes[i][j] == -1:
            visited[i][j] = -1
days = bfs(queue)

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            days = 0
            break
print(days-1)
