import sys

N, M = map(int, sys.stdin.readline().split())
adj_lst = [[] for _ in range(N+1)]
MAX = sys.maxsize
distance = [MAX for _ in range(N+1)]
distance[1] = 0

for i in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    adj_lst[A].append([C, B])

for i in range(1, N):
    for src in range(1, N+1):
        for cost, dest in adj_lst[src]:
            if distance[src] == MAX:
                continue
            if distance[src] + cost < distance[dest]:
                distance[dest] = distance[src] + cost
                if i == N-1:
                    print(-1)
                    exit()

for k in range(2, N+1):
    if distance[k] == MAX:
        print(-1)
    else:
        print(distance[k])
