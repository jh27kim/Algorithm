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


def kruskal(edges, N):
    edges.sort(reverse=True, key=lambda x:[x[2]])
    print(edges)
    answer = 0
    cnt = 0
    while True:
        a, b, cost = edges.pop()
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            answer += cost
            cnt += 1
        print(answer)
        if cnt == N-1:
            return answer



V, E = map(int, input().split())
parent = [i for i in range(V+1)]
edges = list(list(map(int, input().split())) for _ in range(E))
print(kruskal(edges, V))

