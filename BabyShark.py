from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
movement = [[1, 0], [-1, 0], [0, 1], [0, -1]]
size = 2
queue, food = deque(), deque()
cnt, ans, answer = 0, 0, 0


def check():
    for i in range(N):
        for j in range(N):
            if [i, j] in food:
                board[i][j] = 0
                visited[i][j] = 1
                return [i, j]


def check_board(shark):
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0 and board[i][j] < shark:
                return True
    return False


for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            queue.append([i, j])
            board[i][j] = 0
            visited[i][j] = 1

while queue:
    lenq = len(queue)
    while lenq:
        x, y = queue.popleft()
        for m in movement:
            nx, ny = x + m[0], y + m[1]
            if N > nx >= 0 and N > ny >= 0:
                if 0 < board[nx][ny] < size and [nx, ny] not in food:
                    food.append([nx, ny])
                elif (board[nx][ny] == size or not board[nx][ny]) and not visited[nx][ny]:
                    queue.append([nx, ny])
                    visited[nx][ny] = 1
        lenq -= 1
    ans += 1

    if food:
        cnt += 1
        if cnt == size:
            size += 1
            cnt = 0
        if check_board(size):
            answer += ans
            ans = 0
        queue = deque()
        visited = [[0 for _ in range(N)] for _ in range(N)]
        queue.append(check())
        food = deque()
print(answer)
