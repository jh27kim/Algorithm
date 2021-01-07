N, M = map(int, input().split())
maze = [[int(k) for k in input()] for _ in range(N)]

visited = [[0, 0]]
movements = [[1, 0], [-1, 0], [0, 1], [0, -1]]
queue = [[0, 0]]
dist = [[0]*M for _ in range(N)]
dist[0][0] = 1

while queue:
    x, y = queue.pop()
    for i in movements:
        nx = x + i[0]
        ny = y + i[1]
        if N > nx >= 0 and M > ny >= 0:
            if [nx, ny] not in visited and maze[nx][ny] == 1:
                queue.append([nx, ny])
                visited.append([nx, ny])
                dist[nx][ny] = dist[x][y] + 1

print(dist[N-1][M-1])
