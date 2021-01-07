import copy
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
movement = [[1, 0], [-1, 0], [0, 1], [0, -1]]
ans = 0


def bfs():
    global ans
    w = copy.deepcopy(board)
    queue = []
    cnt = 0

    for i in range(N):
        for j in range(M):
            if w[i][j] == 2:
                queue.append([i, j])

    while queue:
        x, y = queue.pop()
        for inx, iny in movement:
            nx, ny = x + inx, y + iny
            if N > nx >= 0 and M > ny >= 0:
                if w[nx][ny] == 0:
                    w[nx][ny] = 2
                    queue.append([nx, ny])

    for i in w:
        for j in i:
            if j == 0:
                cnt += 1
    ans = max(ans, cnt)


def setter(walls):
    if walls == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                setter(walls+1)
                board[i][j] = 0


setter(0)
print(ans)