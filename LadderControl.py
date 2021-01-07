from collections import deque

N, M, H = map(int, input().split())
rows = [list(map(int, input().split())) for _ in range(M)]
rows = [[n[0]-1, n[1]-1] for n in rows]
visited = [[0 for _ in range(N-1)] for _ in range(H)]
queue = deque()
movement = [[1, 0], [-1, 0], [0, 1], [0, -1]]
answer = 4

for x, y in rows:
    visited[x][y] = 1


def dfs(depth, x, y):
    global answer
    if sol():
        answer = min(answer, depth)
        return
    elif depth == 3 or answer <= depth:
        return
    for i in range(x, H):
        k = y if i == x else 0
        for j in range(k, N-1):
            if N-1 > j + 1 and j - 1 >= 0 and H > i >= 0:
                if visited[i][j+1] or visited[i][j-1]:
                    continue
            if not visited[i][j]:
                visited[i][j] = 1
                dfs(depth + 1, i, j+1)
                visited[i][j] = 0


def sol():
    for start in range(N-1):
        k = start
        for i in range(H):
            if k < N-1 and visited[i][k]:
                k += 1
            elif k > 0 and visited[i][k - 1]:
                k -= 1
        if start != k:
            return False
    return True


dfs(0, 0, 0)
print(answer if answer < 4 else -1)


