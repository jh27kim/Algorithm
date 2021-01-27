import copy

board = [[0 for _ in range(4)] for _ in range(4)]
fish_input = list(list(map(int, input().split())) for _ in range(4))
fishes = []
result = 0
movement = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]

for i in range(4):
    for j in range(0, 8, 2):
        fishes.append(fish_input[i][j])
        board[i][j//2] = [fish_input[i][j], fish_input[i][j+1]-1]

fishes.sort()


def turn(direction):
    return (direction+1)%8


def fish_move(board, shark_x, shark_y):
    for fish in fishes:
        location = find(board, fish)
        if location is None:
            continue
        else:
            x, y = location

        d = board[x][y][1]
        for _ in range(8):
            nx, ny = x + movement[d][0], y + movement[d][1]
            if 0 <= nx < 4 and 0 <= ny < 4:
                if not (nx == shark_x and ny == shark_y):
                    board[x][y][1] = d
                    board[nx][ny], board[x][y] = board[x][y], board[nx][ny]
                    break
            d = turn(d)


def find(board, number):
    for x in range(4):
        for y in range(4):
            if board[x][y][0] == number:
                return [x, y]
    return None


def shark_move(board, shark_x, shark_y):
    d = board[shark_x][shark_y][1]
    positions = []
    for _ in range(4):
        shark_x += movement[d][0]
        shark_y += movement[d][1]
        if 0 <= shark_x < 4 and 0 <= shark_y < 4:
            if board[shark_x][shark_y][0] != -1:
                positions.append([shark_x, shark_y])
    return positions


def dfs(board, x, y, total):
    global result
    board = copy.deepcopy(board)

    total += board[x][y][0]
    board[x][y][0] = -1

    fish_move(board, x, y)
    positions = shark_move(board, x, y)

    if len(positions) == 0:
        result = max(result, total)
        return

    for nx, ny in positions:
        dfs(board, nx, ny, total)


dfs(board, 0, 0, 0)
print(result)



