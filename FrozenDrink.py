import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, input())) for _ in range(N)]
answer = 0
visited = [[0 for _ in range(M)] for _ in range(N)]
queue = deque()
movement = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def bfs(queue):
    print("bfs")
    while queue:
        x, y = queue.popleft()
        for m in movement:
            nx, ny = x + m[0], y + m[1]
            print(nx, ny, queue)
            if 0 <= nx < N and 0 <= ny < M:
                if not board[nx][ny] and not visited[nx][ny]:
                    queue.append([nx, ny])
                    visited[nx][ny] = 1
        print(queue)


for i in range(N):
    for j in range(M):
        if not board[i][j] and not visited[i][j]:
            queue.append([i, j])
            visited[i][j] = 1
            answer += 1
            bfs(queue)

print(answer)
