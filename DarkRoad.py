import sys

N, M = map(int, sys.stdin.readline().split())
lights = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
parents = [i for i in range(N)]
lights.sort(key=lambda x:x[2])
answer = 0
total = 0


def find(parents, x):
    if parents[x] != x:
        parents[x] = find(parents, parents[x])
    return parents[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for light in lights:
    x, y, cost = light
    total += cost
    #print(parents, x, y)
    if find(parents, x) != find(parents, y):
        union(parents, x, y)
        answer += cost

print(total - answer)
