from collections import deque

board = [list(input()) for _ in range(8)]
start = [7, 0]
movement = [[0, 0], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1]]
q = deque()
q.append(start)
visited = [[0 for _ in range(8)] for _ in range(8)]


def move(queue):
    nq = deque()
    newwall = ["." for _ in range(8)]
    for i in range(7, 0, -1):
        board[i] = board[i - 1]
    board[0] = newwall

    lenq = len(queue)
    while lenq:
        x, y = queue.popleft()
        if board[x][y] == "#":
            lenq -= 1
            continue
        else:
            nq.append([x, y])
        lenq -= 1
    return nq


def bfs(queue):
    while queue:
        lenq = len(queue)
        while lenq:
            x, y = queue.popleft()
            for m in movement:
                nx, ny = x + m[0], y + m[1]
                if 8 > nx >= 0 and 8 > ny >= 0:
                    if board[nx][ny] == "." and [nx, ny] not in queue:
                        queue.append([nx, ny])
                        visited[nx][ny] = 1
            lenq -= 1
        if visited[0][7]:
            print(1)
            return 0
        queue = move(queue)


bfs(q)
if not visited[0][7]:
    print(0)

