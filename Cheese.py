#세로 가로
from collections import deque
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
queue = deque()
nq = deque()
visited = [[0 for _ in range(m)] for _ in range(n)]
movement = [[1, 0], [-1, 0], [0, 1], [0, -1]]
h = 0

for i in range(n):
    for j in range(m):
        if i == 0 or i == n-1 or j == 0 or j == m-1:
            queue.append([i, j])
            visited[i][j] = 1

while queue:
    x, y = queue.popleft()
    for mv in movement:
        nx, ny = x + mv[0], y + mv[1]
        if n > nx >= 0 and m > ny >= 0:
            if visited[nx][ny] == 0:
                if board[nx][ny] == 1:
                    nq.append([nx, ny])
                else:
                    queue.append([nx, ny])
                visited[nx][ny] = 1
    if not queue:
        queue = nq
        if nq:
            answer = len(nq)
        nq = deque()
        h += 1

print(h-1)
print(answer)
