import itertools
import copy
import sys

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
rotations = [list(map(int, input().split())) for _ in range(K)]
answer = sys.maxsize


def minimum():
    return min(sum(i) for i in b)


def rotate(x, y, d):
    global b
    newboard = copy.deepcopy(b)
    x1, y1, x2, y2 = x-d-1, y-d-1, x+d-1, y+d-1
    #print(x1, y1, x2, y2)
    while x1 != x2:
        for i in range(y1, y2):
            newboard[x1][i+1] = b[x1][i]
        #print(np.asarray(b))
        #print(np.asarray(newboard), "1")
        for j in range(x1, x2):
            newboard[j+1][y2] = b[j][y2]
        #print(np.asarray(b))
        #print(np.asarray(newboard), "2")
        for k in range(y2, y1, -1):
            newboard[x2][k-1] = b[x2][k]
        #print(np.asarray(b))
        #print(np.asarray(newboard), "3")
        for l in range(x2, x1, -1):
            newboard[l-1][y1] = b[l][y1]
        #print(np.asarray(b))
        #print(np.asarray(newboard), "4")
        x1 += 1
        y1 += 1
        x2 -= 1
        y2 -= 1
    return newboard


seq = list(itertools.permutations(rotations, K))
for sq in seq:
    b = copy.deepcopy(board)
    for s in sq:
        b = rotate(s[0], s[1], s[2])
    answer = min(answer, minimum())
print(answer)
