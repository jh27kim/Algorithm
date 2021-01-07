board = [list(map(int, input().split())) for _ in range(10)]
size = list(range(5, 0, -1))
cnt = [5 for _ in range(5)]

for s in range(len(size)):
    for i in range(10-size[s]+1):
        for j in range(10-size[s]+1):
            inc = 0
            for k in range(size[s]):
                if all(v == 1 for v in board[i+k][j:j+size[s]]):
                    inc += 1
            if inc == size[s]:
                for x in range(i, i+size[s]):
                    for y in range(size[s]):
                        board[x][j+y] = 0
                cnt[s] -= 1


if all(s >= 0 for s in cnt):
    print(25-sum(cnt))
else:
    print(-1)
