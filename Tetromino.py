N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

block1 = [[1, 1, 1, 1]]
block2 = [[1, 1],
          [1, 1]]
block3 = [[1, 0],
          [1, 0],
          [1, 1]]
block4 = [[1, 0],
          [1, 1],
          [0, 1]]
block5 = [[1, 1, 1],
          [0, 1, 0]]

tetromino = [block1, block2, block3, block4, block5]
answer = 0


def solve(block):
    global answer

    for _ in range(2):
        for _ in range(4):
            height = len(block)
            width = len(block[0])
            for x in range(N-height+1):
                for y in range(M-width+1):
                    res = 0
                    for i in range(height):
                        for j in range(width):
                            if block[i][j]:
                                res += board[x+i][y+j]
                    answer = max(answer, res)
            block = rotate(block)
        block = flip(block)


def rotate(block):
    height = len(block)
    width = len(block[0])
    new_block = [[0 for _ in range(height)] for _ in range(width)]

    for i in range(height):
        for j in range(width):
            #print(i, j, "-->", j, height-i-1)
            new_block[j][height-i-1] = block[i][j]

    return new_block


def flip(block):
    height = len(block)
    width = len(block[0])
    new_block = [[0 for _ in range(width)] for _ in range(height)]

    for i in range(height):
        for j in range(width):
            new_block[i][width-1-j] = block[i][j]

    return new_block


for block in tetromino:
    solve(block)

print(answer)

