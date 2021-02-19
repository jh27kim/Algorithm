def solution(n, s, a, b, fares):
    answer = int(1e9)
    MAX = int(1e9)
    board = [[MAX if i != j else 0 for i in range(n)] for j in range(n)]
    for c, d, f in fares:
        board[c-1][d-1] = f
        board[d-1][c-1] = f

    for j in range(n):
        for i in range(n):
            if i == j:
                continue
            for k in range(i, n):
                if k == j or k == i:
                    continue
                temp = min(board[i][k], board[i][j] + board[j][k])
                board[i][k] = board[k][i] = temp

    for x in range(n):
        answer = min(answer, board[x][a-1] + board[x][b-1] + board[s-1][x])
        #print(answer, s, x)
        #print('합승:', board[s-1][x])
        #print('A:', board[x-1][s-1])
        #print('B:', board[x - 1][b - 1])
        #print()

    return answer


n = 6
s = 4
a = 5
b = 6
fares = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
print(solution(n, s, a, b, fares))