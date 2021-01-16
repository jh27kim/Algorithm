from collections import deque

K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]
visited = [[[0]*(K+1) for _ in range(W)] for _ in range(H)]
visited[0][0][0] = 1
movement = [[1, 0], [-1, 0], [0, 1], [0, -1]]
jump = [[-2, 1], [1, -2], [1, 2], [2, 1], [2, -1], [-1, 2], [-2, -1], [-1, -2]]
answer = int(1e9)

queue = deque()


def bfs():
    queue.append([0, 0, 0])
    while queue:
        x, y, z = queue.popleft()
        if x == H-1 and y == W-1:
            print(visited[x][y][z]-1)
            return

        if z < K:
            for j in jump:
                nx, ny = x + j[0], y + j[1]
                if 0 <= nx < H and 0 <= ny < W:
                    if not visited[nx][ny][z+1] and not board[nx][ny]:
                        queue.append([nx, ny, z+1])
                        visited[nx][ny][z+1] = visited[x][y][z] + 1

            for m in movement:
                nx, ny = x + m[0], y + m[1]
                if 0 <= nx < H and 0 <= ny < W:
                    if not visited[nx][ny][z] and not board[nx][ny]:
                        queue.append([nx, ny, z])
                        visited[nx][ny][z] = visited[x][y][z] + 1

        elif z == K:
            for m in movement:
                nx, ny = x + m[0], y + m[1]
                if 0 <= nx < H and 0 <= ny < W:
                    if not visited[nx][ny][z] and not board[nx][ny]:
                        queue.append([nx, ny, z])
                        visited[nx][ny][z] = visited[x][y][z] + 1
    print(-1)






def dfs(queue):
    global answer
    loc, cnt, ans = queue[-1]
    x, y = loc

    if [x, y] == [W-1, H-1]:
        answer = min(answer, ans)
        return

    for m in movement:
        nx, ny = x + m[0], y + m[1]
        if 0 <= nx < W and 0 <= ny < H:
            if not visited[nx][ny] and not board[nx][ny]:
                queue.append([[nx, ny], cnt, ans+1])
                visited[nx][ny] = 1
                dfs(queue)
                visited[nx][ny] = 0
                queue.pop()

    if cnt > 0:
        for j in jump:
            nx, ny = x + j[0], y + j[1]
            if 0 <= nx < W and 0 <= ny < H:
                if not visited[nx][ny] and not board[nx][ny]:
                    queue.append([[nx, ny], cnt-1, ans + 1])
                    visited[nx][ny] = 1
                    dfs(queue)
                    visited[nx][ny] = 0
                    queue.pop()

bfs()

