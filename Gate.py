G = int(input())
P = int(input())
parent = [i for i in range(G+1)]


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


for i in range(1, P+1):
    node = find(parent, int(input()))
    if node == 0:
        print(i-1)
    union(parent, node-1, node)
