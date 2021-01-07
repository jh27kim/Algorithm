'''from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
start = [0, 1, 0, 0, 0]
queue = deque()
queue.append(start)
movRight = [[0, 1, 0, 1], [1, 1, 0, 1]]
movDown = [[1, 0, 1, 0], [1, 1, 1, 0]]
movDiag = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 1, 1]]
avail = [[0 for _ in range(N)] for _ in range(N)]
answer = 0

for i in range(N):
    for j in range(N):
        if board[i][j]:
            avail[i][j] = 1
#print(avail)

while queue:
    x1, y1, x2, y2, d = queue.popleft()
    if x1 == N-1 and y1 == N-1:
        answer += 1
        continue
    if d == 0:
        movement = movRight
        nd = 0

    elif d == 1:
        movement = movDown
        nd = 1

    elif d == 2:
        movement = movDiag
        nd = 0
    #print(queue)

    for i1, j1, i2, j2 in movement:
        #print(movement)
        nx1, ny1, nx2, ny2 = x1 + i1, y1 + j1, x2 + i2, y2 + j2
        if N > nx1 >= 0 and N > ny1 >= 0:
            if nd == 2 and not avail[nx1][ny1] and not avail[nx1][ny1-1] and not avail[nx1-1][ny1]:
                queue.append([nx1, ny1, nx2, ny2, nd])
                #print(queue, "diag")
            if nd != 2 and not avail[nx1][ny1]:
                queue.append([nx1, ny1, nx2, ny2, nd])
                #print(queue, "non")
        if d == 0:
            nd += 2
        else:
            nd += 1
    #print(queue, "next")

print(answer)
'''

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
table = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
table[0][1][0] = 1

for x in range(2, n):
    if maps[0][x] == 0:
        table[0][x][0] = table[0][x-1][0]

for y in range(n):
    for x in range(2, n):
        if maps[y][x] == maps[y-1][x] == maps[y][x-1] == 0:
            table[y][x][2] = table[y-1][x-1][2] + table[y-1][x-1][1] + table[y-1][x-1][0]
        if maps[y][x] == 0:
            table[y][x][1] = table[y-1][x][1] + table[y-1][x][2]
            table[y][x][0] = table[y][x-1][0] + table[y][x-1][2]

print(sum(table[-1][-1]))
