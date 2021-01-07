import sys


def find(x):
    if parent[x] == x:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return p


def union(x, y):
    global parent, number
    x, y = find(x), find(y)
    if x != y:
        parent[y] = x
        number[x] += number[y]
    #print(parent)


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
adj_lst = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
costs = []
answer = 0
parent, number = {}, {}

for _ in range(M):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    if a not in parent:
        parent[a] = a
        number[a] = 1
    if b not in parent:
        parent[b] = b
        number[b] = 1
    costs.append([a, b, c])

cnt = 0
for i in range(M):
    costs.sort(key=lambda l: (l[2]), reverse=True)
    x, y, cost = costs.pop()
    if find(y) != find(x):
        cnt += 1
        union(x, y)
        answer += cost
        if cnt == N-1:
            print(answer)
            break

