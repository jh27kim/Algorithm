M, N, K = map(int, input().split())
board = [[0 for _ in range(N)] for _ in range(M)]
boxes = [input().split() for _ in range(K)]

for i in boxes:
    i = [int(x) for x in i]
    x1, y1, x2, y2 = i
    for j in range(M-y2, M-y1):
        for k in range(x1, x2):
            board[j][k] = 1

move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
result = []
visited = []
start = []

while True:
    start = [[i, lst.index(0)] for i, lst in enumerate(board) if 0 in lst][0]
    board[start[0]][start[1]] = 1
    queue = [start]
    answer = 1

    while queue:
        for m in move:
            nx, ny = m[0]+start[0], m[1]+start[1]
            #print(start, nx, ny, board)
            if N > ny >= 0 and M > nx >= 0:
                if board[nx][ny] == 0:
                    queue.append([nx, ny])
                    board[nx][ny] = 1
                    answer += 1
        #print(answer,result, board)
        start = queue.pop()
    result.append(answer)

    if all(elem == board[0] for elem in board):
        break


print(len(result))
result.sort()
print(*result, sep=" ")

#[M-Y-1][X] start
#[M-Y][X-1] end