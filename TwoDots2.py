from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
alphabets = {}
ind = 0
queue = deque()
movement = [[1, 0], [0, 1], [-1, 0], [0, -1]]
done = False


def bfs():
    global done
    while queue:
        x, y, d = queue.popleft()
        #print(x, y, d)
        for m in range(len(movement)):
            if abs(m-d) == 2:
                continue
            nx, ny = x + movement[m][0], y + movement[m][1]
            if N > nx >= 0 and M > ny >= 0:
                if board[nx][ny] == board[i][j]:
                    if visited[nx][ny] == cnt:
                        print('Yes')
                        done = True
                        return
                    queue.append([nx, ny, m])
                    visited[nx][ny] = cnt


cnt = 1
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            queue.append([i, j, -1])
            visited[i][j] = board[i][j]
            bfs()
            cnt += 1
            if done:
                break
    if done:
        break
if not done:
    print("No")
