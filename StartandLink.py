N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
visited = [0 for _ in range(N)]
answer = 99999


def find():
    a, b = 0, 0
    for x in range(len(visited)-1):
        for y in range(x+1, len(visited)):
            if visited[x] * visited[y]:
                a += table[x][y]
                a += table[y][x]
            elif visited[x] + visited[y] == 0:
                b += table[x][y]
                b += table[y][x]
    return abs(a-b)


def dfs(ind, d):
    global answer
    if d == N // 2:
        answer = min(answer, find())
        return

    for i in range(ind, N):
        if not visited[i]:
            visited[i] = 1
            dfs(i+1, d+1)
            visited[i] = 0

dfs(0, 0)
print(answer)
