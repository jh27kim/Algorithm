'''from collections import deque
import copy

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

start = [0, 0]
q1 = deque()
q1.append(start)
movement = [[1, 0], [-1, 0], [0, 1], [0, -1]]
v1 = [board[0][0]]
answer = 0
cnt = 0


def dfs(q, v):
    global answer
    queue = copy.deepcopy(q)
    visited = copy.deepcopy(v)
    x, y = queue.popleft()
    for m in movement:
        nx, ny = x + m[0], y + m[1]
        if R > nx >= 0 and C > ny >= 0:
            if board[nx][ny] not in visited:
                visited.append(board[nx][ny])
                queue.append([nx, ny])
                answer = max(answer, len(visited))
                dfs(queue, visited)
                visited.pop()
                queue.popleft()
    return


dfs(q1, v1)
print(answer)
'''

import sys
# 좌, 하, 우, 상
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def BFS(x, y):
    global answer
    q = set([(x, y, board[x][y])])

    while q:
        print(q)
        x, y, ans = q.pop()
        # 좌우상하 갈 수 있는지 살펴본다
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # index 벗어나지 않는지 체크하고, 새로운 칸이 중복되는 알파벳인지 체크한다
            if ((0 <= nx < R) and (0 <= ny < C)) and (board[nx][ny] not in ans):
                q.add((nx,ny,ans + board[nx][ny]))
                answer = max(answer, len(ans)+1)


R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]

answer = 1
BFS(0, 0)
print(answer)


#########DFS

import sys

# 좌, 하, 우, 상
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def DFS(x, y, ans):
    global answer

    answer = max(ans, answer)

    # 좌우상화 다 확인한다
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # index 벗어나지 않는지 체크하고, 새로운 칸이 중복되는 알파벳인지 체크한다
        if ((0 <= nx < R) and (0 <= ny < C)) and (board[nx][ny] not in passed):
            passed.append(board[nx][ny])
            DFS(nx, ny, ans+1)
            passed.remove(board[nx][ny])



R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]
passed = [board[0][0]]
answer = 1
DFS(0, 0, answer)
print(answer)