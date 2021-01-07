from collections import deque
import copy

N, M = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
board = [list(input()) for _ in range(N)]

q = deque()
q.append([x1 - 1, y1 - 1])

movement = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visited = [[0 for _ in range(M)] for _ in range(N)]
visited[x1 - 1][y1 - 1] = 1


def FirstBFS(fq):
    nq = deque()
    original = copy.deepcopy(fq)
    while fq:
        lenq = len(fq)
        while lenq:
            x, y = fq.popleft()
            for m in movement:
                nx, ny = x + m[0], y + m[1]
                if N > nx >= 0 and M > ny >= 0:
                    if visited[nx][ny] == 0 and board[nx][ny] == "0":
                        visited[nx][ny] = 1
                        fq.append([nx, ny])
                        nq.append([nx, ny])
            lenq -= 1
    if not nq:
        return original
    return nq


def BFS(queue):
    cnt = 0
    while queue:
        lenq = len(queue)
        cnt += 1
        while lenq:
            x, y = queue.popleft()
            for m in movement:
                nx, ny = x + m[0], y + m[1]
                if N > nx >= 0 and M > ny >= 0:
                    if visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        board[nx][ny] = "0"
                        queue.append([nx, ny])
                        if visited[x2 - 1][y2 - 1] == 1:
                            print(cnt)
                            return
            lenq -= 1
        xq = copy.deepcopy(queue)
        candidates = FirstBFS(xq)
        for c in candidates:
            queue.append(c)

BFS(FirstBFS(q))
