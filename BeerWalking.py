from collections import deque

t = int(input())

def bfs(x, y):
    q, c = deque(), []
    q.append([x, y, 20])
    c.append([x, y, 20])
    while q:
        x, y, beer = q.popleft()
        if x == x1 and y == y1:
            print('happy')
            return
        for nx, ny in d:
            if [nx, ny, 20] not in c:
                l1 = abs(nx-x) + abs(ny-y)
                if l1 <= beer*50:
                    q.append([nx, ny, 20])
                    c.append([nx, ny, 20])
    print("sad")
    return

while t:
    n = int(input())
    x0, y0 = map(int, input().split())
    d = []
    for i in range(n):
        x1, y1 = map(int, input().split())
        d.append([x1, y1])
    x1, y1 = map(int, input().split())
    d.append([x1, y1])
    bfs(x0, y0)
    t -= 1

