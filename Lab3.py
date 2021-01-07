from collections import deque
import copy


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
movement = [[1, 0], [-1, 0], [0, 1], [0, -1]]
answer = []


def bfs():
    cnt = 0
    q = copy.deepcopy(queue)
    check = copy.deepcopy(visited)
    while q:
        lenq = len(q)
        while lenq:
            x, y = q.popleft()
            for m in movement:
                nx, ny = x + m[0], y + m[1]
                if N > nx >= 0 and N > ny >=0:
                    if not check[nx][ny] and board[nx][ny] != 1:
                        q.append([nx, ny])
                        check[nx][ny] = 1
                        if board[nx][ny] == 0:
                            last_change = cnt + 1
            lenq -= 1
        cnt += 1
    for x in range(N):
        for y in range(N):
            if check[x][y] == 0 and board[x][y] == 0:
                return -1
    return last_change


def dfs(x1, x2, depth):
    global answer
    if depth == M:
        answer.append(bfs())
        return

    for i in range(x1, N):
        n = x2 if x1 == i else 0
        for j in range(n, N):
            if board[i][j] == 2:
                queue.append([i, j])
                visited[i][j] = 1
                dfs(i, j+1, depth + 1)
                queue.pop()
                visited[i][j] = 0


queue = deque()
dfs(0, 0, 0)

if len(set(answer)) == 1 and answer[0] == -1:
    print(-1)
else:
    print(min(x for x in answer if x > 0))
