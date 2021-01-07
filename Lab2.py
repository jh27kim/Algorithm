import itertools
import copy
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
viruses = []
queue = deque()
movement = [[1, 0], [-1, 0], [0, 1], [0, -1]]
answer = []


def bfs():
    cnt = 0
    while queue:
        lenq = len(queue)
        while lenq:
            x, y = queue.popleft()
            for m in movement:
                nx, ny = x + m[0], y + m[1]
                if N > nx >= 0 and N > ny >= 0:
                    if nboard[nx][ny] == 0:
                        nboard[nx][ny] = 2
                        queue.append([nx, ny])
            lenq -= 1
        cnt += 1
    for i in range(N):
        for j in range(N):
            if nboard[i][j] == 0:
                return -1
    return cnt - 1


for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            board[i][j] = 0
            viruses.append([i, j])

comb = list(itertools.combinations(viruses, M))

for c in comb:
    nboard = copy.deepcopy(board)
    for a, b in c:
        nboard[a][b] = 2
        queue.append([a, b])
    answer.append(bfs())

if len(set(answer)) == 1:
    print(answer[-1])
else:
    print(min([i for i in answer if i > 0]))

