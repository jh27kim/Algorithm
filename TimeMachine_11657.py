MAX = 1e9

N, M = map(int, input().split())
adj_lst = [[] for _ in range(N+1)]
distance = [MAX for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    adj_lst[a].append((b, c))

distance[1] = 0
for _ in range(N-1):
    for x in range(1, N+1):
        for nx, cost in adj_lst[x]:
            if distance[x] == MAX:
                continue
            if distance[x] + cost < distance[nx]:
                distance[nx] = distance[x] + cost

for x in range(1, N+1):
    for nx, cost in adj_lst[x]:
        if distance[x] == MAX:
            continue
        if distance[x] + cost < distance[nx]:
            print(-1)
            exit(0)

if N > 1:
    for i in range(2, N+1):
        print(-1 if distance[i] == MAX else distance[i])

