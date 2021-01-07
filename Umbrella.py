from itertools import permutations

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

N, M = map(int, input().split())
MAP = [list(input()) for _ in range(M)]

# S와 E 모두 X로 바꿔주고 첫항과 끝항으로 배치
X = []
for r in range(M):
    for c in range(N):
        if MAP[r][c] == 'S':
            temp1 = (r, c)
            MAP[r][c] = 'X'
        elif MAP[r][c] == 'E':
            temp2 = (r, c)
            MAP[r][c] = 'X'
        elif MAP[r][c] == 'X':
            X.append((r, c))
X = [temp1] + X + [temp2]

# X 의 간격(link) BFS로 탐색
link = [[float('inf')] * len(X) for _ in range(len(X))]
for i in range(len(X)):
    r, c = X[i]
    visited = [[False] * N for _ in range(M)]
    visited[r][c] = True
    Q = [(r, c, 0)]
    while Q:
        y, x, cnt = Q.pop(0)
        if MAP[y][x] == 'X':
            for j in range(len(X)):
                if X[j] == (y, x):
                    link[i][j] = cnt
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < M and 0 <= nx < N and not visited[ny][nx] and MAP[ny][nx] != '#':
                visited[ny][nx] = True
                Q.append((ny, nx, cnt + 1))

# 모든 경로를 계산하여 최소값 출력
result = float('inf')
for root in permutations(range(1, len(X) - 1)):
    root = [0] + list(root) + [-1]  # S ~ X순열 ~ E
    sub_res = 0
    for i in range(len(X) - 1):
        sub_res += link[root[i]][root[i + 1]]
    if sub_res < result:
        result = sub_res
print(result)