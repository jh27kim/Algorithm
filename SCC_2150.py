def run(x):
    global idid
    parent = idid
    visited[x] = parent
    idid += 1

    print(x)
    stack.append(x)
    for nx in adj_lst[x]:
        if not visited[nx]:
            parent = min(parent, run(nx))
        if not finished[nx]:
            parent = min(parent, visited[nx])

    if parent == visited[x]:
        tmp = []
        while stack:
            t = stack.pop()
            finished[t] = 1
            tmp.append(t)
            if x == t:
                break
        SCC.append(tmp)

    return parent


V, E = map(int, input().split())

adj_lst = [[] for _ in range(V+1)]
for _ in range(E):
    a, b = map(int, input().split())
    adj_lst[a].append(b)

idid = 1
finished = [0 for _ in range(V+1)]
visited = [0 for _ in range(V+1)]
SCC = []
stack = []
run(1)

print(len(SCC))
print(SCC)
