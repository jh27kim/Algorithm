from collections import deque

N, M = map(int, input().split())
adj_lst = [[] for _ in range(N+1)]

#board = [list(map(int, input().split())) for _ in range(N)]
#plan = list(map(int, input().split()))


def dijkstra(start, end):
    queue = deque()
    queue.append(start)
    visited = [0] * N
    visited[start] = 1

    while queue:
        x = queue.popleft()
        for y in range(len(board[x - 1])):
            if board[x][y] and not visited[y]:
                #print(x, y)
                visited[y] = 1
                queue.append(y)
                if y == end:
                    return True
    return False

'''
for i in range(1, len(plan)):
    start = plan[i-1]
    end = plan[i]
    if not dijkstra(start-1, end-1):
        print("NO")
        exit()'''

print("YES")


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    a = find(parent, x)
    b = find(parent, y)

    if a <= b:
        parent[y] = a
    else:
        parent[x] = b


parent = [i for i in range(N+1)]

for i in range(N):
    d = list(map(int, input().split()))
    for j in range(N):
        if d[j]:
            union(parent, i+1, j+1)

result = True
plan = list(map(int, input().split()))

for i in range(len(plan)-1):
    if find(parent, plan[i]) != find(parent, plan[i+1]):
        result = False

print(result)