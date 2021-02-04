import copy

N = int(input())
board = [list(input().split()) for _ in range(N)]


def check():
    detected = False

    for teacher in teachers:
        x, y = teacher
        for dx, dy in movement:
            nx = copy.deepcopy(x)
            ny = copy.deepcopy(y)
            while True:
                nx += dx
                ny += dy
                if 0 <= nx < N and 0 <= ny < N:
                    if board[nx][ny] == 'O':
                        break
                    elif board[nx][ny] == 'S':
                        detected = True
                        break
                else:
                    break

            if detected:
                return True
    return False


def dfs(queue):
    if len(queue) == 3:
        if check():
            return
        print('YES')
        exit()

    for x in range(N):
        for y in range(N):
            if board[x][y] == 'X':
                board[x][y] = 'O'
                queue.append([x, y])
                dfs(queue)
                queue.pop()
                board[x][y] = 'X'


queue = []
teachers = []
movement = [[0, 1], [1, 0], [-1, 0], [0, -1]]

for i in range(N):
    for j in range(N):
        if board[i][j] == 'T':
            teachers.append([i, j])

dfs(queue)
print('NO')
