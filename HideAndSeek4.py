from collections import deque


def solve():
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == k:
            print(visited[x])
            p = []
            while x != n:
                p.append(x)
                x = path[x]
            p.append(n)
            print(" ".join(map(str, p[::-1])))
            return

        for nx in (x + 1, x - 1, 2 * x):
            if 100001 > nx >= 0 and visited[nx] == 0:
                visited[nx] = visited[x] + 1
                path[nx] = x
                queue.append(nx)


n, k = map(int, input().split())
visited = [0 for _ in range(100001)]
path = [0 for _ in range(100001)]
solve()
