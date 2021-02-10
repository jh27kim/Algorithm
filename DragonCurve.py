N = int(input())

def plotcurve(points, g):
    if g == 0:
        #print(points)
        return

    px, py = points[-1]
    rest = points[:-1]
    rest = rest[::-1]

    for x, y in rest:
        x -= px
        y -= py
        nx, ny = -y, x
        nx += px
        ny += py
        board[ny][nx] = 1
        points.append([nx, ny])

    plotcurve(points, g-1)



movement = [[1, 0], [0, -1], [-1, 0], [0, 1]]
board = [[0 for i in range(101)] for _ in range(101)]
answer = 0

for _ in range(N):
    x, y, d, g = map(int, input().split())

    m = movement[d]
    nx, ny = x + m[0], y + m[1]
    board[y][x], board[ny][nx] = 1, 1
    curve = [[x, y], [nx, ny]]

    if g >= 1:
        plotcurve(curve, g)

for i in range(100):
    for j in range(100):
        if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
            answer += 1

print(answer)
