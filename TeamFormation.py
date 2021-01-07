import sys

N, M = map(int, sys.stdin.readline().split())
parent = [i for i in range(N+1)]


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a == b:
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(M):
    inst, a, b = map(int, sys.stdin.readline().split())
    if inst == 0:
        union(parent, a, b)
    else:
        if find(parent, a) == find(parent, b):
            print("YES")
        else:
            print("NO")
