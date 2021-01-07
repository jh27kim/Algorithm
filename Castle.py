from collections import deque

M, N = map(int, input().split())
visited = [[0 for _ in range(M)] for _ in range(N)]
walls = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
sizes = []
mov = [[1, 0], [0, 1], [-1, 0], [0, -1]]
v = [[0 for _ in range(M)] for _ in range(N)]
areas = []


def bfs():
    cnt = 1
    while queue:
        lenq = len(queue)
        while lenq:
            #print(queue, sizes)
            x, y = queue.popleft()
            for m in range(4):
                #print(walls[x][y])
                if walls[x][y][m] == "0":
                    nx, ny = x + mov[m][0], y + mov[m][1]
                    if not visited[nx][ny]:
                        visited[nx][ny] = color
                        queue.append([nx, ny])
                        cnt += 1
            lenq -= 1
    return cnt


def bfsarea(color):
    while queue:
        x, y = queue.popleft()
        for m in mov:
            nx, ny = x + m[0], y + m[1]
            if N > nx >= 0 and M > ny >= 0 and not v[nx][ny]:
                if visited[nx][ny] != color:
                    areas.append(sizes[color-1] + sizes[visited[nx][ny]-1])
                else:
                    queue.append([nx, ny])
                    v[nx][ny] = 1


for i in range(N):
    for j in range(M):
        walls[i][j] = list(bin(walls[i][j])[2:].zfill(4))

# 남 동 북 서
color = 1
for n in range(N):
    for m in range(M):
        if not visited[n][m]:
            queue.append([n, m])
            visited[n][m] = color
            sizes.append(bfs())
            color += 1


for c in range(1, len(sizes)//2+2):
    for x1 in range(N):
        for x2 in range(M):
            if visited[x1][x2] == c:
                queue.append([x1, x2])
                v[x1][x2] = 1
                bfsarea(c)

print(len(sizes))
print(max(sizes))
print(max(areas))

