import sys
from collections import deque


N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
board = [[0 for _ in range(N)] for _ in range(N)]
inst = deque()
m, prev = 3, 0
queue = deque([[0, 0]])
movement = [[-1, 0], [0, -1], [1, 0], [0, 1]]
answer = 0


for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())
    board[x-1][y-1] = 1

L = int(sys.stdin.readline())
for _ in range(L):
    inst.append(input().split())
inst.append([N*N, 'n'])

while True:
    time, d = inst.popleft()

    for i in range(int(time)-prev):
        x, y = queue[-1]
        nx, ny = x + movement[m][0], y + movement[m][1]
        answer += 1
        #print(queue)
        if 0 > nx or nx >= N or 0 > ny or ny >= N:
            print(answer)
            exit()

        if [nx, ny] in queue:
            print(answer)
            exit()

        else:
            if board[nx][ny] == 1:
                board[nx][ny] = 0
            elif board[nx][ny] == 0:
                queue.popleft()
        queue.append([nx, ny])

    prev = int(time)
    if d == 'D':
        m = (m+3)%4
    else:
        m = (m+1)%4
