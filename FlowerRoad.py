N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
movement = [[1, 0], [-1, 0], [0, 1], [0, -1]]
seeds = []
results = []


def check():
    areas = []
    for seed in seeds:
        areas.append(seed)
        for m in movement:
            nx, ny = seed[0] + m[0], seed[1] + m[1]
            if [nx, ny] in areas:
                return False
    return True


def combination(x, y):
    if len(seeds) == 3:
        if check:
            ans = 0
            for s in seeds:
                ans += board[s[0]][s[1]]
                results.append(ans)
        return
    for i in range(x, y):
        for j in range(x, y):
            if [i, j] not in seeds:
                seeds.append([i, j])
                combination(i, j)


for i in range(1, N-1):
    for j in range(1, N-1):
        combination(i, j)
print(min(results))
