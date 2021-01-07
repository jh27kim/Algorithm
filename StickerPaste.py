import sys

N, M, K = map(int, sys.stdin.readline().split())
board = [[0 for i in range(M)] for j in range(N)]


def search(sticker):
    global board
    #print(np.asarray(sticker))
    #print("board")
    #print(np.asarray(board))
    for x in range(N-R+1):
        for y in range(M-C+1):
            thisFit = True
            for r in range(R):
                for c in range(C):
                    if board[x+r][y+c] * sticker[r][c]:
                        thisFit = False
                        break
            if thisFit:
                for x1 in range(R):
                    for y1 in range(C):
                        board[x+x1][y+y1] += sticker[x1][y1]
                return True
    return False


def rotate(sticker):
    #print('rotate')
    sticker = sticker[::-1]
    newSticker = [[0 for _ in range(R)] for _ in range(C)]
    for r in range(R):
        for c in range(C):
            newSticker[c][r] = sticker[r][c]
    return newSticker


for i in range(K):
    R, C = map(int, sys.stdin.readline().split())
    sticker = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
    for j in range(4):
        if not search(sticker):
            sticker = rotate(sticker)
            R, C = C, R
        else:
            break
    #print(np.asarray(board))

print(sum(sum(l) for l in board))
