from collections import deque

N = int(input())
queue = deque()
visited = [[0 for _ in range(N)] for _ in range (N)]
answer = 0
movement = [[1, 1], [1, -1], [-1, 1], [-1, -1]]


def dfs(a, b, n):
    global answer
    if n == N:
        answer += 1
        return

    for i in range(a, N):
        for j in range(b, N):
            if not visited[i][j]:
                queue.append([i, j])
                check(i, j, 1)
                #print(queue)
                #print(np.asarray(visited))
                if j + 1 < N:
                    dfs(i, j+1, n + 1)
                else:
                    dfs(i+1, 0, n + 1)
                queue.pop()
                check(i, j, -1)
                #print(queue)
                #print(np.asarray(visited))
            b = 0


def check(x, y, z):
    for i in range(N):
        visited[x][i] += z
        visited[i][y] += z
    visited[x][y] += (-z)
    for m in movement:
        nx, ny = x + m[0], y + m[1]
        while N > nx >= 0 and N > ny >= 0:
            visited[nx][ny] += z
            nx, ny = nx + m[0], ny + m[1]


dfs(0, 0, 0)
print(answer)
