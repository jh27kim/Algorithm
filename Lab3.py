from collections import deque
import copy

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
movement = [[-1, 0], [0, -1], [1, 0], [0, 1]]
virus = []
queue = deque()
answer = int(1e9)

for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            virus.append([i, j])

checked = [0 for _ in range(len(virus))]


def bfs(queue):
    q = copy.deepcopy(queue)
    visited = [[0 for _ in range(N)] for _ in range(N)]
    total_count, virus_count = 0, 0

    for x, y in q:
        visited[x][y] = 1

    while q:
        lenq = len(q)
        move_flag, blank_flag = 0, 1
        while lenq:
            x, y = q.popleft()
            for m in movement:
                nx, ny = x + m[0], y + m[1]
                if 0 <= nx < N and 0 <= ny < N:
                    if not visited[nx][ny] and board[nx][ny] != 1:
                        visited[nx][ny] = 1
                        q.append([nx, ny])
                        move_flag = 1
                        if not board[nx][ny]:
                            blank_flag = 0
            lenq -= 1

        if move_flag == 1:
            if blank_flag == 0:
                total_count += virus_count + 1
                virus_count = 0

            else:
                virus_count += 1

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and board[i][j] == 0:
                return -1

    return total_count


def dfs(start):
    global answer

    if len(queue) == M:
        res = bfs(queue)
        if res != -1:
            answer = min(answer, res)
        return

    for i in range(start, len(virus)):
        queue.append(virus[i])
        dfs(i+1)
        queue.pop()


dfs(0)
print(-1 if answer == int(1e9) else answer)
