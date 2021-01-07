import sys

N, K = map(int, sys.stdin.readline().split())
backpacks = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 0


def dfs(cnt, weight, value):
    global answer
    if cnt == i:
        return

    for j in range(N):
        if not visited[j] and backpacks[j][0] + weight <= K:
            visited[j] = 1
            value += backpacks[j][1]
            weight += backpacks[j][0]
            #print(answer, value, weight)
            answer = max(answer, value)
            dfs(cnt + 1, weight, value)
            visited[j] = 0
            value -= backpacks[j][1]
            weight -= backpacks[j][0]


for i in range(1, N+1):
    visited = [0 for _ in range(N)]
    dfs(0, 0, 0)
print(answer)
