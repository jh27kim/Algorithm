from collections import deque
import copy

N, L, R = map(int, input().split())
A = [list(map(int, input().split()))for _ in range(N)]
movement = [[1, 0], [-1, 0], [0, 1], [0, -1]]
answer = 0


def bfs(queue, union):
    total = 0

    while queue:
        x, y = queue.popleft()
        total += A[x][y]
        for m in movement:
            nx, ny = x + m[0], y + m[1]
            if 0 <= nx < N and 0 <= ny < N:
                if L <= abs(A[nx][ny] - A[x][y]) <= R and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])
                    union.append([nx, ny])

    p = total // len(union)
    for i, j in union:
        A[i][j] = p


def migrate(union, population):
    population = population // len(union)
    for x, y in union:
        A[x][y] = population


queue = deque()

while True:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    total_union = []
    #new_A = copy.deepcopy(A)
    time = 0

    for x in range(N):
        for y in range(N):
            if not visited[x][y]:
                visited[x][y] = 1
                queue.append([x, y])
                bfs(queue, [[x, y]])
                #migrate(union, population)
                time += 1
    if time == N*N:
        break
    #A = new_A
    answer += 1

print(answer)
