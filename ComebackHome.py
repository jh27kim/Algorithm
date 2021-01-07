from collections import deque
import copy

R, C, K = map(int, input().split())
board = [list(input()) for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
visited[R-1][0] = 1
movement = [[-1, 0], [1, 0], [0, 1], [0, -1]]
queue = deque()
queue.append([R-1, 0])
answer = 0


def solve(queue, v1):
    global answer
    v = copy.deepcopy(v1)
    q = copy.deepcopy(queue)
    x, y = q.popleft()

    for ix, iy in movement:
        nx, ny = x + ix, y + iy
        #print(v, sum((sum(x) for x in v)), [x, y], [nx, ny], [ix, iy])

        if R > nx >= 0 and C > ny >= 0:
            if board[nx][ny] == "." and v[nx][ny] == 0:
                v[nx][ny] = 1
                queue.insert(0, [nx, ny])
                dist = sum((sum(x) for x in v))
                if [nx, ny] == [0, C-1] and dist == K:
                    answer += 1
                    return
                solve(queue, v)
                v[nx][ny] = 0
    return

solve(queue, visited)
print(answer)
