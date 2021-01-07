from collections import deque
import copy

N = int(input())
board = [list(input()) for _ in range(N)]
blind = copy.deepcopy(board)
colors = ['R', 'G', 'B']
answer = [0 for _ in range(3)]
answer2 = [0 for _ in range(3)]
movement = [[1, 0], [-1, 0], [0, 1], [0, -1]]
queue = deque()


def bfs(b):
    while queue:
        x, y = queue.popleft()
        for m in movement:
            nx, ny = x + m[0], y + m[1]
            if N > nx >= 0 and N > ny >= 0:
                if b[nx][ny] == c:
                    b[nx][ny] = 0
                    queue.append([nx, ny])


for l in range(N):
    for k in range(N):
        if board[l][k] == "G":
            blind[l][k] = "R"

ind = 0
for c in colors:
    for i in range(N):
        for j in range(N):
            if board[i][j] == c:
                queue.append([i, j])
                board[i][j] = 0
                bfs(board)
                answer[ind] += 1
    ind += 1

ind = 0
for c in colors:
    for i in range(N):
        for j in range(N):
            if blind[i][j] == c:
                queue.append([i, j])
                board[i][j] = 0
                bfs(blind)
                answer2[ind] += 1
    ind += 1

print(sum(answer), sum(answer2))
