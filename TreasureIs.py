from collections import deque
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
queue = deque()
movement = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visited = [[0 for _ in range(M)] for _ in range(N)]
w = 0


def bfs(q):
    cnt = 0
    nq = deque()
    while q:
        x, y = q.popleft()
        for m in movement:
            nx, ny = x + m[0], y + m[1]
            if N > nx >= 0 and M > ny >= 0:
                if board[nx][ny] == 'L' and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    nq.append([nx, ny])
        if not q:
            q = nq
            cnt += 1
            nq = deque()
    return cnt


for i in range(N):
    for j in range(M):
        if board[i][j] == 'L' and not visited[i][j]:
            queue.append([i, j])
            visited[i][j] = 1
            w = max(w, bfs(queue))
print(w)
