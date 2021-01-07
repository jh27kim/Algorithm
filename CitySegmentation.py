import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
edges = []
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    edges.append([A, B, C])

edges.sort(reverse=True, key=lambda x:x[2])
cnt, answer =0, []
queue = deque()
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


while N-1:
    a, b, c = edges.pop()
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        answer.append(c)
        N -= 1

print(answer)
answer.sort()
print(sum(answer) - answer[-1])
