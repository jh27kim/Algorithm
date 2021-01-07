def mul(l1, l2):
    res = [[0 for _ in range(len(l1[0]))] for _ in range(len(l2))]
    for i in range(len(l1)):
        for j in range(len(l1[0])):
            res[i][j] = l1[i][j] * l2[i][j]
    return res


def rotate():
    global sticker
    sticker = list(zip(*sticker[::-1]))


def pasteSticker(sticker):
    global board
    width, height = len(sticker[0]), len(sticker)

    for x in range(N-height+1):
        for y in range(M-width+1):
            lst = [board[r][y:y+width] for r in range(x, x+height)]
            res = mul(lst, sticker)
            if all(all(v == 0 for v in sublist) for sublist in res):
                for x1 in range(height):
                    for y1 in range(width):
                        if sticker[x1][y1]:
                            board[x+x1][y+y1] = 1
                return True
    return False


N, M, K = map(int, input().split())
board = [[0 for _ in range(M)] for _ in range(N)]

for i in range(K):
    R, C = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(R)]

    for t in range(4):
        if pasteSticker(sticker):
            break
        else:
            rotate()

print(sum(sum(l) for l in board))
