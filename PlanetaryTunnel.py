import sys

N = int(sys.stdin.readline().rstrip())
coordinates = []
edges = []
parent = [i for i in range(N)]


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

x, y, z = [], [], []

for i in range(N):
    x1, y1, z1 = list(map(int, sys.stdin.readline().split()))
    x.append((x1, i))
    y.append((y1, i))
    z.append((z1, i))

x.sort()
y.sort()
z.sort()

for i in range(N-1):
    edges.append((abs(x[i][0]-x[i+1][0]), x[i][1], x[i+1][1]))
    edges.append((abs(y[i][0] - y[i + 1][0]), y[i][1], y[i + 1][1]))
    edges.append((abs(z[i][0] - z[i + 1][0]), z[i][1], z[i + 1][1]))

edges.sort()
answer = 0

for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        answer += cost

print(answer)



