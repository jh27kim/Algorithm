import heapq

T = int(input())
for _ in range(T):
    N = int(input())
    MAX = int(1e9)

    board = [list(map(int, input().split())) for _ in range(N)]
    distance = [[MAX for _ in range(N)] for _ in range(N)]
    distance[0][0] = board[0][0]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    queue = []
    heapq.heappush(queue, [distance[0][0], 0, 0])

    while queue:
        d, x, y = heapq.heappop(queue)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                cost = d + board[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(queue, [distance[nx][ny], nx, ny])

    print(distance[-1][-1])
