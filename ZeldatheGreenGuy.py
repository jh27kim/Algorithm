import heapq

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
MAX = int(1e9)
cnt = 0

while True:
    N = int(input())
    if N == 0:
        break
    cnt += 1

    distance = [[MAX for _ in range(N)] for _ in range(N)]
    board = [list(map(int, input().split())) for _ in range(N)]
    distance[0][0] = board[0][0]

    queue = []
    heapq.heappush(queue, [distance[0][0], 0, 0])

    while queue:
        c, x, y = heapq.heappop(queue)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if c + board[nx][ny] < distance[nx][ny]:
                    distance[nx][ny] = c + board[nx][ny]
                    #print(np.asarray(distance))
                    heapq.heappush(queue, [distance[nx][ny], nx, ny])

    print('Problem', str(cnt)+':', distance[-1][-1])
