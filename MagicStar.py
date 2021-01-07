board = [list(input()) for _ in range(5)]
check = [0 for _ in range(12)]
done = False
#import numpy as np

for i in range(5):
    for j in range(9):
        if board[i][j].isupper():
            check[ord(board[i][j])-65] = 1


def finish():
    n1, n2, n3, n4, n5, n6 = 0, 0, 0, 0, 0, 0
    for m in range(4):
        n1 += ord(board[m][4-m])-64
        n2 += ord(board[3][2*m+1])-64
        n3 += ord(board[3-m][7-m])-64
        n4 += ord(board[1][2*m+1])-64
        n5 += ord(board[m+1][m+1])-64
        n6 += ord(board[4-m][4+m])-64
    if n1 == n2 == n3 == n4 == n5 == n6 == 26:
        return True


def dfs(n):
    global board, done
    if done:
        return

    #print(check)
    #print(np.asarray(board))
    if n == 12:
        if finish():
            for b in board:
                print("".join(b))
            done = True
        return
    for c in range(len(check)):
        if check[c] == 0:
            alphabet = chr(c+65)
            break
    for x in range(5):
        for y in range(9):
            if board[x][y] == "x":
                board[x][y] = alphabet
                check[c] = 1
                dfs(n+1)
                board[x][y] = "x"
                check[c] = 0


dfs(sum(check))
