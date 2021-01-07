from collections import deque

F, S, G, U, D = map(int, input().split())
visited = [0 for _ in range(F)]

queue = deque()
queue.append(S)
cnt = -1
visited[S-1] = 1

while queue:
    lenq = len(queue)
    while lenq:
        x = queue.popleft()
        nx, nx2 = x + U, x - D
        if F >= nx > 0 and not visited[nx-1]:
            queue.append(nx)
            visited[nx-1] = 1
        if F >= nx2 > 0 and not visited[nx2-1]:
            queue.append(nx2)
            visited[nx2-1] = 1
        lenq -= 1
    cnt += 1

if visited[G-1]:
    print(cnt)
else:
    print('use the stairs')
