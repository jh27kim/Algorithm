from collections import deque
N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
queue.append([0, 0])
visited = [[0 for _ in range(N)] for _ in range(N)]
visited[0][0] = 1
movement = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def bfs():
    population = board[0][0]
    land = 1
    answer = 0
    global answer
    while queue:
        x, y = queue.popleft()
        for m in movement:
            nx, ny = x + m[0], y + m[1]
            if N > nx >= 0 and N > ny >= 0:
                if L <= abs(board[x][y] - board[nx][ny]) <= R and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])
                    population += board[nx][ny]
                    land += 1

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                board[i][j] = population // land


print(board)
