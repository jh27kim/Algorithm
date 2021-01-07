from collections import deque

N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
visited[0][0] = 1
queue = deque()
queue.append([0, 0])
princess = [N-1, M-1]
movement = [[1, 0], [-1, 0], [0, 1], [0, -1]]
sword = T+1


def bfs():
    global sword
    while queue:
        lenq = len(queue)
        while lenq:
            x, y = queue.popleft()
            if board[x][y] == 2:
                sword = N - 1 - x + M - 1 - y + visited[x][y] - 1
            if [x, y] == princess:
                return min(visited[x][y] - 1, sword)
            for m in movement:
                nx, ny = x + m[0], y + m[1]
                if N > nx >= 0 and M > ny >= 0:
                    if board[nx][ny] != 1 and not visited[nx][ny]:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append([nx, ny])
            lenq -= 1
    return sword


ans = bfs()
print(ans if ans <= T else "Fail")
