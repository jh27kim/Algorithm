from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
movement = [[1, 0], [-1, 0], [0, 1], [0, -1]]
queue, islands = deque(), deque()
visited = [[0 for _ in range(N)] for _ in range(N)]


def bfs():
    nq = deque()
    while queue:
        lenq = len(queue)
        while lenq:
            x, y = queue.popleft()
            for m in movement:
                nx, ny = x + m[0], y + m[1]
                if N > nx >= 0 and N > ny >= 0:
                    if board[nx][ny] == 1 and not visited[nx][ny]:
                        queue.append([nx, ny])
                        visited[nx][ny] = 1
                    elif board[nx][ny] == 0 and [x, y] not in nq:
                        nq.append([x, y])
            lenq -= 1
    return nq


for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and not visited[i][j]:
            queue.append([i, j])
            visited[i][j] = 1
            islands.append(bfs())


answer = N*N

for i in range(len(islands)):
    for x1, y1 in islands[i]:
        for j in range(i+1, len(islands)):
            for x2, y2 in islands[j]:
                answer = min(answer, abs(x2 - x1) + abs(y2 - y1) - 1)
print(answer)
