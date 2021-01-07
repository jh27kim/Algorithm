N = int(input())
curve = [list(map(int, input().split())) for _ in range(N)]
board = [[0 for _ in range(101)] for _ in range(101)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def rotate(p, n):
    #print(p, n)
    tx, ty = n[1]-p[1], n[0]-p[0]
    nx1 = -ty + p[1]
    ny1 = tx + p[0]
    return [ny1, nx1]


def sol():
    cnt = 0
    for i in range(100):
        for j in range(100):
            if board[i][j] and board[i][j+1] and board[i+1][j] and board[i+1][j+1]:
                #print(board[i][j], board[i][j+1], board[i+1][j], board[i+1][j+1])
                #print(i, j)
                cnt += 1
    return cnt


for x, y, d, g in curve:
    nx, ny = x + dx[d], y + dy[d]
    nodes = [[y, x], [ny, nx]]
    board[y][x], board[ny][nx] = 1, 1
    pivot = [ny, nx]
    while g:
        #print("nodes", nodes)
        for i in range(0, len(nodes)):
            n = rotate(pivot, nodes[i])
            if n not in nodes:
                nodes.append(n)
        #nodes.append(pivot)
        pivot = rotate(pivot, nodes[0])
        g -= 1
    for y1, x1 in nodes:
        board[y1][x1] = 1
    #print(nodes)
print(sol())

