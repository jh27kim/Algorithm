from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
queue = deque()
queue.append([0, 0, False])
visited = [[0 for _ in range(M)] for _ in range(N)]
visited[0][0] = 1
movement = [[1, 0], [-1, 0], [0, 1], [0, -1]]

while queue:
    x, y, w = queue.popleft()
    if [x, y] == [N-1, M-1]:
        break
    for m in movement:
        nx, ny = x + m[0], y + m[1]
        if N > nx >= 0 and M > ny >= 0:
            if not visited[nx][ny]:
                if board[nx][ny] == 1 and not w:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny, True])
                if board[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny, w])

if not visited[N-1][M-1]:
    print('-1')
else:
    print(visited[N - 1][M - 1])
