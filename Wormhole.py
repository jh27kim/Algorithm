T = int(input())
MAX = int(1e9)

for _ in range(T):
    cycle = False
    N, M, W = map(int, input().split())
    adj_lst = [[] for _ in range(N+1)]
    for _ in range(M):
        start, end, cost = map(int, input().split())
        adj_lst[start].append([end, cost])
        adj_lst[end].append([start, cost])
    for _ in range(W):
        start, end, cost = map(int, input().split())
        adj_lst[start].append([end, -cost])

    start = 1
    distance = [MAX for _ in range(N+1)]
    distance[start] = 0

    for i in range(1, N+1):
        for j in range(1, N+1):
            for end, cost in adj_lst[j]:
                new_cost = distance[j] + cost
                if new_cost < distance[end]:
                    distance[end] = new_cost
                    if i == N:
                        cycle = True

    if cycle:
        print('YES')
    else:
        print('NO')
