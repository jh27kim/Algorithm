import sys

answer = sys.maxsize
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
queue = []


def check(queue):
    start = 0
    link = 0
    link_team = [1 for _ in range(N)]

    for i in range(N//2):
        link_team[queue[i]] = 0
        for j in range(i+1, N//2):
            x, y = queue[i], queue[j]
            start += board[x][y]
            start += board[y][x]

    for i in range(N):
        for j in range(i+1, N):
            if link_team[i] and link_team[j]:
                link += board[i][j]
                link += board[j][i]
    return abs(start - link)


def dfs(queue, x):
    global answer

    if len(queue) == N//2:
        answer = min(answer, check(queue))
        return

    for i in range(x, N):
        queue.append(i)
        dfs(queue, i+1)
        queue.pop()


dfs(queue, 0)
print(answer)
