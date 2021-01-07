N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]


def check(x, y):
    print(x, y)
    for m in range(N-x):
        for n in range(M-y):
            box = []
            for x1 in range(y):
                box.append(board[m][n+x1])
                box.append(board[m + x][n+y-x1])
                print([m, n+x1], '1')
                print([m + x, n + y - x1], "3")
            for y1 in range(x):
                print([y1+m, n + y], "2")
                box.append(board[m+y1][n+y])
                box.append(board[m+x-y1][n])
                print([m+x-y1, n], "4")
            print(box)

    if len(set(box)) == 1:
        return True
    else:
        return False


ind = False
for i in range(1, N):
    for j in range(1, M):
        if check(i, j):
            print('Yes')
            ind = True
            break
if not ind:
    print("No")

print(all(['a', 'b']))