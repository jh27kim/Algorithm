from _collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    indegree = [0] * (n+1)
    board = [[0 for _ in range(n+1)] for _ in range(n+1)]
    data = list(map(int, input().split()))

    for i in range(len(data)):
        for j in range(i+1, len(data)):
            board[data[i]][data[j]] = 1
            indegree[data[j]] += 1

    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        if board[a][b]:
            board[a][b] = False
            board[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            board[a][b] = True
            board[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    result = []
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    cycle = False
    certain = True

    for i in range(n):
        if not q:
            cycle = True
            break

        if len(q) >= 2:
            certain = False
            break

        now = q.popleft()
        result.append(now)

        for j in range(1, n+1):
            if board[now][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

    if cycle:
        print('IMPOSSIBLE')
    elif not certain:
        print('?')
    else:
        print(*result)
